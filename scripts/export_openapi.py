from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def export_openapi(output_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))
    from rock_music_generator.main import app

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(app.openapi(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Export the FastAPI OpenAPI schema.")
    parser.add_argument(
        "output_path",
        nargs="?",
        default="docs/api/openapi.json",
        type=Path,
    )
    args = parser.parse_args()
    export_openapi(args.output_path)


if __name__ == "__main__":
    main()
