from fastapi.testclient import TestClient

from rock_music_generator.main import app


def main() -> None:
    client = TestClient(app)
    prompt = (
        "Песня о человеке, который уезжает из города "
        "и начинает новую жизнь"
    )
    response = client.post(
        "/v1/tracks",
        json={
            "prompt": prompt,
            "genre": "rock",
            "language": "ru",
            "lyrics_mode": "generate",
            "duration_sec": 10,
            "target_audio_mode": "instrumental_with_lyrics_file",
        },
    )
    response.raise_for_status()
    job_id = response.json()["job_id"]
    status = client.get(f"/v1/tracks/{job_id}")
    status.raise_for_status()
    print(status.json())


if __name__ == "__main__":
    main()
