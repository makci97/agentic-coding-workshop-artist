## Родительский PRD

[materials/prd/0002-geometric-patterns.md](../../prd/0002-geometric-patterns.md)

## Что строим

Создать директорию `patterns/` с базовыми JSON-конфигами для трёх типов паттернов: спираль, мандала, сетка.

## Критерии выполненной задачи

- [ ] Создана директория `patterns/`
- [ ] `spiral.json` — конфиг спирали с полями: name, pattern_type, center, max_radius, colors, stroke_width, params.spirals, params.density
- [ ] `mandala.json` — конфиг мандалы с полями: name, pattern_type, center, max_radius, colors, stroke_width, params.num_spokes, params.layers
- [ ] `grid.json` — конфиг сетки с полями: name, pattern_type, center, size, colors, stroke_width, params.rows, params.cols
- [ ] Все цвета в форматах hex (#RRGGBB)
- [ ] Конфиги валидны и готовы к использованию

## Блокируется

Нет — можно начинать сразу
