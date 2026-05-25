FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --no-cache-dir ".[dev]"

COPY rock_music_generator ./rock_music_generator
COPY docs ./docs
COPY README.md AGENTS.md ./

ENV ARTIFACT_ROOT=/app/artifacts
EXPOSE 8000

CMD ["uvicorn", "rock_music_generator.main:app", "--host", "0.0.0.0", "--port", "8000"]
