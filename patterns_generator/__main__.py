"""Main entry point for patterns generator CLI.

Usage:
    python -m patterns_generator <config.json>
"""

import sys
from pathlib import Path

from dotenv import load_dotenv

# Load .env file from project root
load_dotenv()

from patterns_generator.client import CanvasClient, create_client_from_env
from patterns_generator.config import load_pattern
from patterns_generator.generators import (
    generate_grid,
    generate_mandala,
    generate_spiral,
)


GENERATORS = {
    "spiral": generate_spiral,
    "mandala": generate_mandala,
    "grid": generate_grid,
}


def main() -> int:
    """Main entry point.

    Returns:
        Exit code (0 for success, non-zero for error).
    """
    if len(sys.argv) != 2:
        print("Usage: python -m patterns_generator <config.json>")
        return 1

    config_path = Path(sys.argv[1])
    if not config_path.exists():
        print(f"Error: Config file not found: {config_path}")
        return 1

    # Load and validate config
    try:
        config = load_pattern(config_path)
        print(f"Loaded config: {config.name} ({config.pattern_type})")
    except Exception as e:
        print(f"Error loading config: {e}")
        return 1

    # Generate strokes
    generator = GENERATORS.get(config.pattern_type)
    if generator is None:
        print(f"Error: Unknown pattern type: {config.pattern_type}")
        print(f"Available types: {', '.join(GENERATORS.keys())}")
        return 1

    strokes = generator(config)
    print(f"Generated {len(strokes)} strokes")

    # Create client and send
    try:
        client = create_client_from_env()
        print(f"Connecting to {client.ws_url} as '{client.artist_name}'...")

        # Register artist
        if client.register_artist():
            print("Artist registered successfully")
        else:
            print("Artist already registered")

        # Connect and send
        with client:
            client.send_strokes(strokes)
            print(f"Sent {len(strokes)} strokes to server")

    except Exception as e:
        print(f"Error sending to server: {e}")
        return 1

    print("Done!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
