"""WebSocket client for sending strokes to the canvas server."""

import json
import os
from dataclasses import dataclass

import requests
import websocket


@dataclass
class Stroke:
    """Represents a single stroke segment."""

    x1: float
    y1: float
    x2: float
    y2: float
    color: str
    w: float


class CanvasClient:
    """Client for connecting to canvas server and sending strokes."""

    def __init__(self, ws_url: str, artist_name: str):
        """Initialize canvas client.

        Args:
            ws_url: WebSocket URL (e.g., ws://195.133.25.57/canvas/ws)
            artist_name: Artist name for registration
        """
        self.ws_url = ws_url
        self.artist_name = artist_name
        self.ws: websocket.WebSocket | None = None

    def register_artist(self) -> bool:
        """Register artist on the server.

        Returns:
            True if registration successful, False if conflict.

        Raises:
            requests.HTTPError: If registration fails with 422 or other error.
        """
        # Derive HTTP URL from WebSocket URL for registration
        http_url = self.ws_url.replace("ws://", "http://").replace(
            "wss://", "https://"
        )
        # Determine if using test canvas
        is_test = http_url.endswith("/canvas/ws-test")
        # Build registration URL: http://host/canvas/register or /canvas/register-test
        if is_test:
            base_url = http_url.replace("/canvas/ws-test", "")
            register_url = f"{base_url}/canvas/register-test"
        else:
            base_url = http_url.replace("/canvas/ws", "")
            register_url = f"{base_url}/canvas/register"

        response = requests.post(
            register_url, json={"artist_name": self.artist_name}, timeout=10
        )

        if response.status_code == 200:
            return True
        if response.status_code == 409:
            return False  # Already registered
        response.raise_for_status()
        return False

    def connect(self) -> None:
        """Establish WebSocket connection."""
        self.ws = websocket.create_connection(self.ws_url)

    def send_strokes(self, strokes: list[Stroke]) -> None:
        """Send strokes to the server.

        Args:
            strokes: List of Stroke objects to send.
        """
        if self.ws is None:
            raise RuntimeError("Not connected. Call connect() first.")

        segments = [
            {
                "x1": s.x1,
                "y1": s.y1,
                "x2": s.x2,
                "y2": s.y2,
                "color": s.color,
                "w": s.w,
            }
            for s in strokes
        ]

        message = {"artist_name": self.artist_name, "segments": segments}
        self.ws.send(json.dumps(message))

    def close(self) -> None:
        """Close WebSocket connection."""
        if self.ws:
            self.ws.close()
            self.ws = None

    def __enter__(self) -> "CanvasClient":
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.close()


def create_client_from_env() -> CanvasClient:
    """Create CanvasClient from environment variables.

    Returns:
        CanvasClient configured with SERVER_WS_URL and ARTIST_NAME from .env.
    """
    ws_url = os.getenv("SERVER_WS_URL", "ws://195.133.25.57/canvas/ws")
    artist_name = os.getenv("ARTIST_NAME", "artist")
    return CanvasClient(ws_url, artist_name)
