from fastapi import APIRouter

from .rooms.router import router as rooms_router


def get_router() -> APIRouter:
    router = APIRouter(prefix="/v1")
    router.include_router(rooms_router)
    return router
