from fastapi import Depends

from app.api.dependencies.stub import Stub
from app.shared.config import Config
from app.shared.services.livekit.api_adapter import LivekitAPIAdapter


async def get_livekit_api_adapter(config: Config = Depends(Stub(Config))) -> LivekitAPIAdapter:
    adapter = LivekitAPIAdapter(config.providers.livekit)
    try:
        yield adapter
    finally:
        await adapter.close()
