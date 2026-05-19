## Родительский PRD

[materials/prd/0002-geometric-patterns.md](../../prd/0002-geometric-patterns.md)

## Что строим

Модуль загрузки и валидации JSON-конфигов. `patterns_generator/config.py` с функциями `load_pattern()` и `validate_config()`, возвращающими dataclass `PatternConfig`.

## Критерии выполненной задачи

- [x] Создан пакет `patterns_generator/` с `__init__.py`
- [x] Dataclass `PatternConfig` с полями: name, pattern_type, center, max_radius, colors, stroke_width, rotation_angle, params
- [x] Функция `load_pattern(path: str) -> PatternConfig` — читает JSON, вызывает валидацию
- [x] Функция `validate_config(config: dict) -> PatternConfig` — проверяет обязательные поля, применяет значения по умолчанию
- [x] Валидация отклоняет конфиги без name, pattern_type, colors
- [x] Тесты на некорректные конфиги (пустой файл, missing required fields, invalid types)

## Блокируется

- `002-create-pattern-configs.md` — нужны примеры конфигов для тестов
