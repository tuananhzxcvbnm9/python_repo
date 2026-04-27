from fastapi import APIRouter
from app.schemas.auth import LoginRequest, TokenPair
from app.auth.jwt import create_token
from app.core.config import settings

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/register')
def register(payload: LoginRequest) -> dict[str, str]:
    return {"email": payload.email, "message": "registered"}

@router.post('/login', response_model=TokenPair)
def login(payload: LoginRequest) -> TokenPair:
    return TokenPair(
        access_token=create_token(payload.email, settings.jwt_secret, 30, 'access'),
        refresh_token=create_token(payload.email, settings.jwt_secret, 60*24*7, 'refresh'),
    )

@router.post('/refresh', response_model=TokenPair)
def refresh(payload: LoginRequest) -> TokenPair:
    return login(payload)

@router.get('/me')
def me() -> dict[str, str]:
    return {"email": "admin@example.com", "role": "admin"}
