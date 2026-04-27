from fastapi import Header, HTTPException

def require_role(role: str):
    def checker(x_role: str = Header(default="member")) -> str:
        if x_role not in {"admin", "manager", "member", "support_agent", "customer"}:
            raise HTTPException(status_code=403, detail="invalid role")
        return x_role
    return checker
