## Родительский PRD

[materials/prd/0002-geometric-patterns.md](../../prd/0002-geometric-patterns.md)

## Что строим

Генераторы паттернов в `patterns_generator/generators.py`. Три функции для генерации спиралей, мандал и сеток. Возвращают список штрихов с координатами и цветами.

## Критерии выполненной задачи

- [ ] Dataclass `Stroke` с полями: x1, y1, x2, y2, color, w
- [ ] `generate_spiral(config: PatternConfig) -> list[Stroke]` — генерирует спиральные линии от центра
- [ ] `generate_mandala(config: PatternConfig) -> list[Stroke]` — генерирует радиально-симметричный узор
- [ ] `generate_grid(config: PatternConfig) -> list[Stroke]` — генерирует сетку линий
- [ ] Координаты в пределах холста (0..800, 0..600 по умолчанию)
- [ ] Детерминированность: одинаковый конфиг → одинаковый результат
- [ ] Модульные тесты: каждый генератор возвращает непустой список
- [ ] Тесты на диапазоны координат (все x, y в пределах canvas)

## Блокируется

- `003-config-loader.md` — нужен PatternConfig для импорта
