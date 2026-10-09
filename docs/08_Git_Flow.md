# Git Flow проекта SportShop

```text
main  ────────────────●────────────────●  стабильная версия
  \                    \              /
   develop ─●────●───────●────●────────●  интеграционная ветка
             \    \             \  /
          feature/*  конфликт      hotfix/*
```

- `main` содержит стабильную версию; срочные исправления попадают сюда через `hotfix/*`.
- `develop` объединяет готовые функции перед выпуском.
- Каждая функция разрабатывается в `feature/<название>` и после проверки вливается в `develop`.
- Для учебного PR ветка `feature/search-advanced` оставлена отдельно для ревью.
- Ветка `hotfix/cart-total` создаётся от `main`, после исправления вливается и в `main`, и в `develop`.

В этом упражнении созданы ветки `develop`, `feature/low-stock`, `feature/total-v1`, `feature/total-v2`, `feature/search-advanced` и `hotfix/cart-total`.
