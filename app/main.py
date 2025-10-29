from fastapi import FastAPI, Depends

from api.router import api_router
from core.security import get_api_key

app = FastAPI(
    title="Справочник организаций",
    description="RESP API с реализованными методами",
    docs_url="/docs",
)

app.include_router(api_router, dependencies=[Depends(get_api_key)])


@app.get("/health")
async def health():
    return {"status": "ok"}
