## Родительский PRD

[materials/prd/0002-geometric-patterns.md](../../prd/0002-geometric-patterns.md)

## Что строим

WebSocket клиент для отправки штрихов на сервер. `patterns_generator/client.py` с классом `CanvasClient` для подключения, регистрации и отправки.

## Критерии выполненной задачи

- [x] Класс `CanvasClient(ws_url: str, artist_name: str)`
- [x] Метод `register_artist() -> bool` — POST /canvas/register, обработка 200/409/422
- [x] Метод `send_strokes(strokes: list[Stroke])` — отправка через WebSocket
- [x] Метод `close()` — корректное закрытие соединения
- [x] Конфигурация из `.env`: SERVER_WS_URL, ARTIST_NAME
- [x] Интеграционные тесты на test-канвасе (/canvas/ws-test)
- [x] Тест на регистрацию артиста (успех, конфликт)

## Блокируется

Нет — можно начинать сразу
