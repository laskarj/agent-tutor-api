from fastapi import APIRouter, FastAPI

from app.api import v1

main_router = APIRouter(prefix="/api")


@main_router.get("/status")
def get_status():
    return {"status": "ok"}


def setup(app: FastAPI) -> None:
    v1_router = v1.get_router()
    main_router.include_router(v1_router)

    app.include_router(main_router)
