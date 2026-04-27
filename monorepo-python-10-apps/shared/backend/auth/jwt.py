from datetime import datetime, timedelta, timezone
import jwt

def create_token(subject: str, secret: str, minutes: int, token_type: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": subject, "type": token_type, "iat": now, "exp": now + timedelta(minutes=minutes)}
    return jwt.encode(payload, secret, algorithm="HS256")
