import os
from functools import lru_cache
from pathlib import Path


class Settings:
    app_name: str = os.getenv("APP_NAME", "rock-music-generator")
    artifact_root: Path = Path(os.getenv("ARTIFACT_ROOT", "artifacts"))
    default_backend: str = os.getenv("DEFAULT_BACKEND", "mock")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
