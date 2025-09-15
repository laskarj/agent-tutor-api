from livekit.agents import JobProcess
from livekit.plugins import silero

from app.shared.logger import get_logger

logger = get_logger("agent.prewarming")


class PrewarmingService:
    """Service for prewarming resources."""

    @staticmethod
    def prewarm(proc: JobProcess):
        logger.info("Prewarming VAD model...")
        proc.userdata["vad"] = silero.VAD.load()
        logger.info("Prewarming completed")
