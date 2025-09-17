from livekit.agents import AgentSession, RoomInputOptions, metrics, JobContext

from app.agent.assistant.agent import Assistant
from app.agent.session.config import SessionConfig
from app.agent.session.handlers import SessionHandlers
from app.shared.logger import get_logger

logger = get_logger("agent.session")


class SessionManager:
    """Manages agent session lifecycle."""

    def __init__(self, ctx: JobContext) -> None:
        self.ctx = ctx
        self.usage_collector = metrics.UsageCollector()
        self.session = None
        self.handlers = None

    async def create_session(self):
        config = SessionConfig()

        self.session = AgentSession(
            llm=config.get_llm_config(),
            stt=config.get_stt_config(),
            tts=config.get_tts_config(),
            turn_detection=config.get_turn_detection_config(),
            vad=config.load_vad(),
            preemptive_generation=config.get_preemptive_generation(),
        )

        self.handlers = SessionHandlers(self.session, self.usage_collector)
        self.ctx.add_shutdown_callback(self._log_usage)
        return self.session

    async def start_session(self):
        await self.session.start(
            agent=Assistant(),
            room=self.ctx.room,
            room_input_options=RoomInputOptions(),
        )

    async def _log_usage(self):
        summary = self.usage_collector.get_summary()
        logger.info(f"Usage: {summary}")
