from fastapi import Header, HTTPException
from auth import verify_token

def get_current_user(
    authorization: str = Header(None)
):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Token Missing"
        )

    token = authorization.split(" ")[1]

    user_id = verify_token(token)

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    return user_id