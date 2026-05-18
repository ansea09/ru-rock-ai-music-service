# ru-rock-ai-music-service

Local REST service for generating Russian rock songs with automatically generated lyrics.

## Current status
MVP scaffold. API contract, job schema, eval rubric are defined.
Music generation is initially stubbed and will be replaced by ACE-Step worker.

## Demo goal
Input: Russian prompt + genre=rock.
Output: generated lyrics, audio candidate(s), selected candidate, eval manifest.

## Architecture
- FastAPI REST API
- Redis queue
- Lyrics worker
- ACE-Step music worker
- Eval worker
- Object storage
- FPF evidence and parity documents

## Quickstart
```bash
cp .env.example .env
make install
make test
make api
