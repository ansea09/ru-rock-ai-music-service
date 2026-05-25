from fastapi.testclient import TestClient

from rock_music_generator.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_mock_generation_lifecycle() -> None:
    create = client.post(
        "/v1/tracks",
        json={
            "prompt": "Песня о дороге домой",
            "genre": "rock",
            "language": "ru",
            "lyrics_mode": "generate",
            "duration_sec": 10,
            "target_audio_mode": "instrumental_with_lyrics_file",
        },
    )
    assert create.status_code == 202
    job_id = create.json()["job_id"]

    status = client.get(f"/v1/tracks/{job_id}")
    assert status.status_code == 200
    body = status.json()
    assert body["status"] == "completed"
    assert body["metadata"]["actual_audio_mode"] == "instrumental_with_lyrics_file"

    lyrics = client.get(f"/v1/tracks/{job_id}/lyrics")
    assert lyrics.status_code == 200
    assert "Песня о дороге домой" in lyrics.json()["lyrics"]

    audio = client.get(f"/v1/tracks/{job_id}/audio")
    assert audio.status_code == 200
    assert audio.headers["content-type"].startswith("audio/wav")


def test_rejects_aligned_lyrics_for_mock_backend() -> None:
    response = client.post(
        "/v1/tracks",
        json={
            "prompt": "Песня с проверенным вокалом",
            "target_audio_mode": "sung_lyrics_aligned",
        },
    )
    assert response.status_code == 422
