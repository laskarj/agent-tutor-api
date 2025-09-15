from livekit.agents import Agent, RunContext
from livekit.agents.llm import function_tool

from app.shared.logger import get_logger

logger = get_logger("agent.assistant")


class Assistant(Agent):
    """Voice AI Assistant."""

    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a helpful voice AI assistant.
            You eagerly assist users with their questions by providing information from your extensive knowledge.
            Your responses are concise, to the point, and without any complex formatting or punctuation including
            emojis, asterisks, or other symbols.
            You are curious, friendly, and have a sense of humor.""",
        )

    @function_tool
    async def lookup_example(self, context: RunContext, key_word_example: str):
        """Look up current information."""
        # TODO: Integrate with real  API
        return "info example."
