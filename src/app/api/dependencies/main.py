from functools import partial

from fastapi import FastAPI

from app.api.dependencies.providers import get_livekit_api_adapter
from app.api.dependencies.stub import Stub
from app.shared.config import Config, load_config
from app.shared.services.livekit.api_adapter import LivekitAPIAdapter


def setup(app: FastAPI) -> None:
    app.dependency_overrides[Stub(Config)] = partial(load_config, Config)
    app.dependency_overrides[Stub(LivekitAPIAdapter)] = get_livekit_api_adapter
