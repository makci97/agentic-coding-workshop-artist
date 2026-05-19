"""Smoke-тесты для canvas.html viewer.

Проверка корректности парсинга query-параметров и базовой функциональности.
"""

import re
from pathlib import Path


def test_canvas_html_exists():
    """HTML-файл вьюера существует."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    assert canvas_path.exists(), f"canvas.html not found at {canvas_path}"


def test_canvas_has_canvas_element():
    """HTML содержит <canvas> элемент."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "<canvas" in content, "No <canvas> element found"
    assert 'id="canvas"' in content or "id='canvas'" in content, "Canvas has no id"


def test_canvas_fullscreen():
    """Canvas занимает весь экран через CSS."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    # Проверка стилей canvas
    assert "margin: 0" in content or "margin:0" in content, "No margin: 0"
    assert "overflow: hidden" in content or "overflow:hidden" in content, "No overflow: hidden"


def test_websocket_connection_code():
    """Код содержит WebSocket подключение."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "WebSocket" in content, "No WebSocket code found"
    assert "ws://" in content, "No ws:// URL found"


def test_default_ws_url():
    """Default WebSocket URL настроен правильно."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    # Проверка default URL
    assert "ws://195.133.25.57/canvas/ws" in content, "Default WS URL not found"


def test_query_param_parsing():
    """Парсинг query-параметра ws из URL."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "URLSearchParams" in content, "No URLSearchParams found"
    assert "window.location.search" in content, "No location.search parsing"
    assert "params.get('ws')" in content or 'params.get("ws")' in content, "No ws param parsing"


def test_ws_url_validation():
    """Валидация WebSocket URL (ws:// или wss://)."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "ws://" in content and "startsWith" in content, "No WS URL validation"


def test_canvas_config_fetch():
    """Fetch для получения конфигурации canvas."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "fetch" in content, "No fetch API found"
    assert "/canvas/config" in content, "No /canvas/config endpoint"


def test_message_handling():
    """Обработка WS сообщений: open, snapshot, delta, clear."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "'open'" in content or '"open"' in content, "No 'open' message handling"
    assert "'snapshot'" in content or '"snapshot"' in content, "No 'snapshot' handling"
    assert "'delta'" in content or '"delta"' in content, "No 'delta' handling"
    assert "'clear'" in content or '"clear"' in content, "No 'clear' handling"


def test_canvas_rendering():
    """Рендеринг через Canvas 2D API."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "getContext('2d')" in content or 'getContext("2d")' in content, "No 2D context"
    assert "moveTo" in content, "No moveTo for drawing"
    assert "lineTo" in content, "No lineTo for drawing"
    assert "stroke" in content, "No stroke call"


def test_stroke_storage():
    """Хранение штрихов в массиве."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    # Проверка хранения strokes
    assert "strokes" in content, "No strokes array"
    assert "push" in content, "No push to strokes"


def test_reconnect_on_close():
    """Автоматическое переподключение при разрыве."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "onclose" in content, "No onclose handler"
    assert "setTimeout" in content or "setInterval" in content, "No reconnect timer"


def test_error_handling():
    """Обработка ошибок WebSocket."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "onerror" in content, "No onerror handler"
    assert "error" in content.lower(), "No error handling"


def test_server_error_message():
    """Обработка серверных ошибок {type: 'error'}."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    # Проверка обработки error сообщений от сервера
    assert "'error'" in content or '"error"' in content, "No error message type handling"


# =============================================================================
# Error Handling & Reconnect Tests
# =============================================================================

def test_connection_indicator_exists():
    """Индикатор подключения существует."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "connection-indicator" in content, "No connection-indicator"
    assert "connectionStatus" in content, "No connectionStatus element"


def test_connection_status_states():
    """Статусы подключения: connected, disconnected, reconnecting."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "connected" in content, "No connected state"
    assert "disconnected" in content, "No disconnected state"
    assert "reconnecting" in content, "No reconnecting state"


def test_connection_indicator_styling():
    """Индикатор подключения имеет стили."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert ".connection-indicator" in content, "No connection-indicator CSS"
    assert "position: absolute" in content or "position:absolute" in content, "No absolute positioning"


def test_error_display_exists():
    """Отображение ошибок существует."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "error-display" in content, "No error-display"
    assert "errorMessage" in content, "No errorMessage element"


def test_exponential_backoff():
    """Exponential backoff для переподключения."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    # Проверка exponential backoff
    assert "Math.pow" in content or "**" in content, "No exponential calculation"
    assert "MAX_RECONNECT_DELAY" in content, "No max delay constant"
    assert "reconnectAttempts" in content, "No reconnectAttempts counter"


def test_jitter_in_reconnect():
    """Jitter добавляется к задержке переподключения."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "Math.random" in content, "No jitter in reconnect delay"


def test_update_connection_status_function():
    """Функция updateConnectionStatus существует."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "updateConnectionStatus" in content, "No updateConnectionStatus function"


def test_show_hide_error_functions():
    """Функции showError/hideError существуют."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    assert "showError" in content, "No showError function"
    assert "hideError" in content, "No hideError function"


def test_error_message_displayed():
    """Текст ошибки отображается пользователю."""
    canvas_path = Path(__file__).parent.parent.parent / "canvas" / "canvas.html"
    content = canvas_path.read_text()

    # Проверка отображения ошибки
    assert "errorMessage.textContent" in content or 'errorMessage.textContent =' in content, "No error message display"
    assert "errorDisplay.classList.add" in content or 'errorDisplay.classList.add(' in content, "No error display show"
