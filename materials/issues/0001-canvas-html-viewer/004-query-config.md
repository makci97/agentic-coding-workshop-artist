## Родительский PRD

[materials/prd/0001-canvas-html-viewer.md](../../prd/0001-canvas-html-viewer.md)

## Что строим

Конфигурация WebSocket URL через query-параметр. Парсинг `?ws=...` из `window.location.search`, валидация URL, fallback на default URL, поддержка обоих канвасов (main/test).

## Критерии выполненной задачи

- [ ] Парсинг query-параметра `ws` из URL
- [ ] Валидация WebSocket URL (начинается с `ws://` или `wss://`)
- [ ] Fallback на default URL при отсутствии параметра
- [ ] Поддержка main канваса: `ws://195.133.25.57/canvas/ws`
- [ ] Поддержка test канваса: `ws://195.133.25.57/canvas/ws-test`
- [ ] Документация в README или комментарии в коде

## Блокируется

Нет — можно начинать сразу
