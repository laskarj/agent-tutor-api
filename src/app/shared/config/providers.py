from dataclasses import dataclass


@dataclass(frozen=True)
class LivekitConfig:
    ws_url: str
    api_key: str
    secret_key: str


@dataclass(frozen=True)
class OpenAPIConfig:
    secret_key: str


@dataclass(frozen=True)
class ProvidersConfig:
    livekit: LivekitConfig
    openapi: OpenAPIConfig
