from fastapi import Header, HTTPException
from starlette import status

from app.core.config import settings


def get_api_key(api_key: str = Header(...)):
    if api_key == settings.API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return api_key
