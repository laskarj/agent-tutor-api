from livekit.plugins import openai
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from app.shared.config import load_config
from app.shared.config.providers import ProvidersConfig


class SessionConfig:
    """Configuration for agent session."""

    def __init__(self) -> None:
        self.__cfg: ProvidersConfig = load_config(ProvidersConfig, config_scope="providers")

    def get_llm_config(self):
        return openai.LLM(model="gpt-4o-mini", api_key=self.__cfg.openapi.secret_key)

    def get_stt_config(self):
        return openai.STT(model="whisper-1", language="en", api_key=self.__cfg.openapi.secret_key)

    def get_tts_config(self):
        return openai.TTS(voice="nova", api_key=self.__cfg.openapi.secret_key)

    @staticmethod
    def get_turn_detection_config():
        return MultilingualModel()

    @staticmethod
    def get_preemptive_generation():
        return True
