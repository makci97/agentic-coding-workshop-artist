## Родительский PRD

[materials/prd/0002-geometric-patterns.md](../../prd/0002-geometric-patterns.md)

## Что строим

Генераторы паттернов в `patterns_generator/generators.py`. Три функции для генерации спиралей, мандал и сеток. Возвращают список штрихов с координатами и цветами.

## Критерии выполненной задачи

- [x] Dataclass `Stroke` с полями: x1, y1, x2, y2, color, w
- [x] `generate_spiral(config: PatternConfig) -> list[Stroke]` — генерирует спиральные линии от центра
- [x] `generate_mandala(config: PatternConfig) -> list[Stroke]` — генерирует радиально-симметричный узор
- [x] `generate_grid(config: PatternConfig) -> list[Stroke]` — генерирует сетку линий
- [x] Координаты в пределах холста (0..800, 0..600 по умолчанию)
- [x] Детерминированность: одинаковый конфиг → одинаковый результат
- [x] Модульные тесты: каждый генератор возвращает непустой список
- [x] Тесты на диапазоны координат (все x, y в пределах canvas)

## Блокируется

- `003-config-loader.md` — нужен PatternConfig для импорта
