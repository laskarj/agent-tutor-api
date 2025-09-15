from livekit.agents import WorkerOptions, cli

from app.shared.config import Config, load_config
from app.shared.logger import get_logger, setup_logging

from .worker.entrypoint import EntrypointHandler
from .worker.prewarming import PrewarmingService

setup_logging("DEBUG")
logger = get_logger("agent.cli")


def main():
    """Main CLI entry point for LiveKit agent."""

    config = load_config(Config)

    logger.info("Starting LiveKit agent...")
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=EntrypointHandler.handle,
            prewarm_fnc=PrewarmingService.prewarm,
            ws_url=config.providers.livekit.ws_url,
            api_secret=config.providers.livekit.secret_key,
            api_key=config.providers.livekit.api_key,
        )
    )


if __name__ == "__main__":
    main()
