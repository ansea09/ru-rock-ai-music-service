from fastapi import FastAPI

from rock_music_generator.api.routes import router
from rock_music_generator.core.config import settings

app = FastAPI(
    title="Local Russian Rock Music Generation API",
    version="0.1.0",
    description="Prototype API scaffold with a deterministic mock backend.",
)
app.include_router(router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok", "version": app.version, "app_name": settings.app_name}
