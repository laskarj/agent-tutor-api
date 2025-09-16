from fastapi import FastAPI

from app.api import dependencies, exceptions, router_registry
from app.shared.logger import setup_logging


def create_app() -> FastAPI:
    _app = FastAPI()
    setup_logging("DEBUG")
    dependencies.setup(_app)
    exceptions.setup_exception_handlers(_app)
    router_registry.setup(_app)
    return _app
