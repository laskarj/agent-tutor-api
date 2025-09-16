from fastapi import FastAPI

from app.api.router_registry import main_router


def create_app() -> FastAPI:
    _app = FastAPI()
    _app.include_router(main_router)
    return _app
