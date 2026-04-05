from fastapi import Header, HTTPException

def get_role(x_role: str = Header(...)):
    if x_role not in ["ADMIN", "ANALYST", "VIEWER"]:
        raise HTTPException(status_code=400, detail="Invalid role")
    return x_role


def require_admin(role: str):
    if role != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin access required")


def require_analyst_or_admin(role: str):
    if role not in ["ADMIN", "ANALYST"]:
        raise HTTPException(status_code=403, detail="Not authorized")