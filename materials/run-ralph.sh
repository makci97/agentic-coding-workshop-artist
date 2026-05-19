#!/usr/bin/env bash
# Запускает ralph-loop, который ходит по issue в materials/issues/.
set -euo pipefail
# cd "$(dirname "$0")/.."

exec claude \
  --permission-mode bypassPermissions \
  --model large \
  "/ralph-loop:ralph-loop \"Возьми следующую невыполненную issue из materials/issues/. 
  Создай отдельный branch, реализуй задачу: строго проходи по критериям, отметь \\\`[x]\\\` прямо в файле. 
  После выполненной задачи сделай пуллреквест в main branch, проверь отсутсвие конфликтов и переключись обратно в main, обнови его. 
  Закрыл — переходи к следующей. 
  Перед переходом к следующей задаче проверь через gh, что закрыты PR для всех задач, от которых зависит следующая.
  Пока не закрыты - жди. Проверяй раз в 10 секунд.
  Когда все issue в папке закрыты — выведи <promise>DONE</promise>. 
  Не ври, не комить.\" --completion-promise 'DONE' --max-iterations 50"
