from livekit.agents import AgentFalseInterruptionEvent, MetricsCollectedEvent, NOT_GIVEN, metrics

from app.shared.logger import get_logger

logger = get_logger("agent.handlers")


class SessionHandlers:
    """Event handlers for agent session."""

    def __init__(self, session, usage_collector):
        self.session = session
        self.usage_collector = usage_collector
        self._setup_handlers()

    def _setup_handlers(self):
        self.session.on("agent_false_interruption")(self._on_agent_false_interruption)
        self.session.on("metrics_collected")(self._on_metrics_collected)

    def _on_agent_false_interruption(self, ev: AgentFalseInterruptionEvent):
        logger.info("false positive interruption, resuming")
        self.session.generate_reply(instructions=ev.extra_instructions or NOT_GIVEN)

    def _on_metrics_collected(self, ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        self.usage_collector.collect(ev.metrics)
