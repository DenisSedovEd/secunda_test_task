from fastapi import APIRouter

from app.api.v1 import activities, buildings, organizations

api_router = APIRouter()
api_router.include_router(buildings.router, prefix="/buildings", tags=["building"])
api_router.include_router(activities.router, prefix="/activities", tags=["activities"])
api_router.include_router(
    organizations.router, prefix="/organizations", tags=["organizations"]
)
