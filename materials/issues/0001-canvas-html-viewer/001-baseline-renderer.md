## Родительский PRD

[materials/prd/0001-canvas-html-viewer.md](../../prd/0001-canvas-html-viewer.md)

## Что строим

Минимальный работающий вьюер: HTML-каркас с `<canvas>` на весь экран, подключение к WebSocket, получение размеров холста через `/canvas/config`, обработка сообщений `open` → `snapshot` → `delta`, рендеринг всех штрихов через Canvas 2D API. Без UI слоёв и индикаторов.

## Критерии выполненной задачи

- [ ] HTML-файл с `<canvas>` элементом на весь экран
- [ ] GET `/canvas/config` → получение `{ width, height }`, инициализация canvas
- [ ] WebSocket подключение (default URL: `ws://195.133.25.57/canvas/ws`)
- [ ] Обработка сообщений: `open`, `snapshot`, `delta`
- [ ] Рендеринг штрихов через Canvas 2D API (`moveTo`, `lineTo`, `stroke`)
- [ ] Перерисовка при получении `delta`
- [ ] Очистка canvas при получении `clear`
- [ ] Тесты на Canvas Renderer согласно «Решения по тестированию» родительского PRD

## Блокируется

Нет — можно начинать сразу
