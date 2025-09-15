from dataclasses import dataclass

from app.shared.config.providers import ProvidersConfig


@dataclass(frozen=True)
class Config:
    providers: ProvidersConfig
