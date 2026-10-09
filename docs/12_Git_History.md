# История Git

Снимок вывода `git log --oneline --graph --all` после слияния hotfix и перед коммитом самого отчёта:

```text
*   9a70237 merge: hotfix/cart-total → develop
|\  
| | * ca11761 docs: добавлена имитация pull request
| | * 0d6ffbd US-2: добавлен расширенный поиск товаров
| |/  
|/|   
* | 1976309 docs: описано разрешение конфликта
* |   7e5c8d1 Разрешён конфликт в total_sum
|\ \  
| * | 685dc34 feature: total_sum с учётом количества
* | |   26c22cd merge: feature/total-v1 → develop
|\ \ \  
| |/ /  
|/| |   
| * | 82d8298 feature: total_sum без учёта количества
|/ /  
* |   7cd953e merge: feature/low-stock → develop
|\ \  
| * | 6810b67 US-1: добавлена функция get_low_stock
|/ /  
* | c2101c5 docs: описана схема Git Flow
| | * 65f95e2 merge: hotfix/cart-total → main
| |/| 
|/|/  
| * 60308de docs: описан процесс hotfix
| * b17bdab hotfix: cart_total учитывает количество
|/  
* df59cd8 chore: начальная версия SportShop
```

## Анализ
- Создано 5 рабочих веток: `feature/low-stock`, `feature/total-v1`, `feature/total-v2`, `feature/search-advanced`, `hotfix/cart-total`; кроме них использовались `main` и `develop`.
- В `develop` слиты низкий остаток, `feature/total-v1`, `feature/total-v2` (после ручного разрешения конфликта) и hotfix. Hotfix также слит в `main`.
- Конфликт возник в `shop.py` на функции `total_sum`: обе feature-ветки изменили одну строку. Оставлен вариант с учётом количества и создан отдельный коммит.
- `feature/search-advanced` оставлена для имитации PR; остальные feature/hotfix ветки удалены после слияния.

Примечание: этот файл показывает историю непосредственно перед собственным коммитом отчёта, поэтому последующий коммит `docs: добавлен отчёт о Git-истории` в блоке выше ещё не отображён.
