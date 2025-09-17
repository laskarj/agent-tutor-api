from livekit.agents import JobContext

from app.agent.session.manager import SessionManager
from app.shared.logger import get_logger

logger = get_logger("agent.entrypoint")


class EntrypointHandler:
    """Main entrypoint handler for the agent."""

    @staticmethod
    async def handle(ctx: JobContext):
        ctx.log_context_fields = {"room": ctx.room.name}
        logger.info(f"Starting agent session for room: {ctx.room.name}")

        session_manager = SessionManager(ctx)
        await session_manager.create_session()
        await session_manager.start_session()
        await ctx.connect()

        logger.info("Agent session started successfully")
