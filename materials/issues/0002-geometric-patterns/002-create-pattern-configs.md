## Родительский PRD

[materials/prd/0002-geometric-patterns.md](../../prd/0002-geometric-patterns.md)

## Что строим

Создать директорию `patterns/` с базовыми JSON-конфигами для трёх типов паттернов: спираль, мандала, сетка.

## Критерии выполненной задачи

- [x] Создана директория `patterns/`
- [x] `spiral.json` — конфиг спирали с полями: name, pattern_type, center, max_radius, colors, stroke_width, params.spirals, params.density
- [x] `mandala.json` — конфиг мандалы с полями: name, pattern_type, center, max_radius, colors, stroke_width, params.num_spokes, params.layers
- [x] `grid.json` — конфиг сетки с полями: name, pattern_type, center, size, colors, stroke_width, params.rows, params.cols
- [x] Все цвета в форматах hex (#RRGGBB)
- [x] Конфиги валидны и готовы к использованию

## Блокируется

Нет — можно начинать сразу
