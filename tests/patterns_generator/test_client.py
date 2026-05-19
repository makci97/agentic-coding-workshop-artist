"""Tests for patterns_generator.client module."""

import os
import random
import string

import pytest

from patterns_generator.client import CanvasClient, Stroke, create_client_from_env


def new_test_artist_name() -> str:
    """Generate unique artist name for tests."""
    return "test" + "".join(random.choices(string.ascii_letters, k=15))


class TestStrokeDataclass:
    """Tests for Stroke dataclass."""

    def test_stroke_creation(self):
        """Stroke can be created with required fields."""
        stroke = Stroke(x1=0, y1=0, x2=100, y2=100, color="#FF0000", w=2.0)
        assert stroke.x1 == 0
        assert stroke.y1 == 0
        assert stroke.x2 == 100
        assert stroke.y2 == 100
        assert stroke.color == "#FF0000"
        assert stroke.w == 2.0


class TestCanvasClient:
    """Tests for CanvasClient class."""

    def test_client_initialization(self):
        """CanvasClient initializes with ws_url and artist_name."""
        client = CanvasClient("ws://localhost:8000/ws", "test_artist")
        assert client.ws_url == "ws://localhost:8000/ws"
        assert client.artist_name == "test_artist"
        assert client.ws is None

    def test_register_artist_conflict(self):
        """register_artist returns False on conflict (409)."""
        # Use test canvas
        client = CanvasClient("ws://195.133.25.57/canvas/ws-test", "demo")
        # First registration should succeed or already exist
        client.register_artist()
        # Second registration should return False (conflict)
        result = client.register_artist()
        assert result is False  # Already registered


class TestCreateClientFromEnv:
    """Tests for create_client_from_env function."""

    def test_with_env_vars(self, monkeypatch):
        """create_client_from_env uses environment variables."""
        monkeypatch.setenv("SERVER_WS_URL", "ws://test:8000/ws")
        monkeypatch.setenv("ARTIST_NAME", "env_artist")

        client = create_client_from_env()
        assert client.ws_url == "ws://test:8000/ws"
        assert client.artist_name == "env_artist"

    def test_with_defaults(self, monkeypatch):
        """create_client_from_env uses defaults when env vars missing."""
        monkeypatch.delenv("SERVER_WS_URL", raising=False)
        monkeypatch.delenv("ARTIST_NAME", raising=False)

        client = create_client_from_env()
        assert client.ws_url == "ws://195.133.25.57/canvas/ws"
        assert client.artist_name == "artist"


class TestCanvasClientContextManager:
    """Tests for CanvasClient context manager."""

    def test_context_manager(self):
        """CanvasClient can be used as context manager."""
        client = CanvasClient("ws://195.133.25.57/canvas/ws-test", new_test_artist_name())
        # Context manager should connect and close
        # Note: This test may fail if server is unavailable
        try:
            with client as c:
                assert c.ws is not None
        except Exception:
            pytest.skip("Server unavailable for context manager test")
