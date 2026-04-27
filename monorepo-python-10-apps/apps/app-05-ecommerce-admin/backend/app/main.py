import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
from app.core.logging import configure_logging
from app.api.routes.health import router as health_router
from app.api.routes.auth import router as auth_router
from app.api.routes.orders import router as entity_router
from app.monitoring.metrics import REQUEST_COUNT, REQUEST_LATENCY, metrics_response

configure_logging()
app = FastAPI(title='E-commerce Admin API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv('CORS_ORIGINS', 'http://localhost').split(','),
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.middleware('http')
async def metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    REQUEST_COUNT.labels(path=request.url.path, method=request.method).inc()
    REQUEST_LATENCY.labels(path=request.url.path).observe(time.perf_counter() - start)
    return response

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(entity_router)

@app.get('/metrics')
def metrics():
    return metrics_response()
