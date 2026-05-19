# artist

Стартовый репозиторий воркшопа. Пишем Python-кисти, палитры и работы — рисуем на общий канвас.

## Сервер

- API: <http://195.133.25.57>
- OpenAPI: <http://195.133.25.57/openapi>
- Общий канвас (вьюер): <http://195.133.25.57/canvas/view>
- Тестовый канвас (вьюер): <http://195.133.25.57/canvas/view-test>

## Команды

```bash
uv sync               # установить зависимости
just install-hooks    # pre-commit hooks
just audit            # ruff + pyright + tach
just fix              # auto-fix
just test             # прогнать интеграционный тест против сервера
```

## Canvas Viewer

HTML-вьюер для отображения общего канваса. Поддерживает конфигурацию через query-параметры:

- `ws=<url>` — WebSocket URL (обязательно `ws://` или `wss://`)
- `http=<url>` — HTTP base URL для `/canvas/config`
- `canvas=main|test` — выбор канваса (`main` по умолчанию, `test` для `/ws-test`)

Примеры:
- `canvas/view?canvas=main` — основной канвас
- `canvas/view?canvas=test` — тестовый канвас
- `canvas/view?ws=ws://localhost:3000/canvas/ws` — кастомный WebSocket

Архитектура и контракт сервера — в [CLAUDE.md](CLAUDE.md).
