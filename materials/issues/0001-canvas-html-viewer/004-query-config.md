## Родительский PRD

[materials/prd/0001-canvas-html-viewer.md](../../prd/0001-canvas-html-viewer.md)

## Что строим

Конфигурация WebSocket URL через query-параметр. Парсинг `?ws=...` из `window.location.search`, валидация URL, fallback на default URL, поддержка обоих канвасов (main/test).

## Критерии выполненной задачи

- [x] Парсинг query-параметра `ws` из URL
- [x] Валидация WebSocket URL (начинается с `ws://` или `wss://`)
- [x] Fallback на default URL при отсутствии параметра
- [x] Поддержка main канваса: `ws://195.133.25.57/canvas/ws`
- [x] Поддержка test канваса: `ws://195.133.25.57/canvas/ws-test`
- [x] Документация в README или комментарии в коде

## Блокируется

Нет — можно начинать сразу
