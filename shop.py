"""Функции каталога и заказов для учебного проекта «СпортТовары»."""

import json
from pathlib import Path
from typing import Any
from collections.abc import Iterable


def _total_stock(product: dict[str, Any]) -> int:
    """Возвращает остаток с учётом вариантов представления товара."""
    if "stocks" in product:
        stocks = product["stocks"]
        if isinstance(stocks, dict):
            return sum(int(value) for value in stocks.values())
        return sum(int(item.get("quantity", 0)) for item in stocks)
    return int(product.get("quantity", product.get("stock", 0)))


def get_low_stock(products: Iterable[dict[str, Any]], limit: int = 3) -> list[dict[str, Any]]:
    """Выбирает товары с суммарным остатком не выше limit, по возрастанию."""
    matches = [product for product in products if _total_stock(product) <= limit]
    return sorted(matches, key=lambda product: (_total_stock(product), str(product.get("name", "")).casefold()))


def search_advanced(
    products: Iterable[dict[str, Any]],
    query: str = "",
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> list[dict[str, Any]]:
    """Ищет по названию/бренду и одновременно применяет заданные фильтры."""
    if not query.strip():
        return []
    needle = query.casefold().strip()
    result = []
    for product in products:
        searchable = f"{product.get('name', '')} {product.get('brand', '')}".casefold()
        if needle not in searchable:
            continue
        if category is not None and str(product.get("category", "")).casefold() != category.casefold():
            continue
        price = float(product.get("price", 0))
        if min_price is not None and price < min_price:
            continue
        if max_price is not None and price > max_price:
            continue
        result.append(product)
    return result


def count_by_category(products: Iterable[dict[str, Any]]) -> dict[str, int]:
    """Подсчитывает число товарных записей в каждой категории."""
    counts: dict[str, int] = {}
    for product in products:
        category = str(product.get("category", "Без категории"))
        counts[category] = counts.get(category, 0) + 1
    return counts


def save_orders(orders: Any, filename: str | Path = "orders.json") -> None:
    """Сохраняет заказы в JSON с поддержкой кириллицы."""
    with Path(filename).open("w", encoding="utf-8") as file:
        json.dump(orders, file, ensure_ascii=False, indent=2)


def cart_total(items):
    """Сумма позиций корзины (исходная версия для упражнения hotfix)."""
    return sum(float(item.get("price", 0)) * int(item.get("quantity", 1)) for item in items)


def total_sum(products):
    """Итоговая стоимость единиц товара (будет уточнена при разрешении конфликта)."""
    return sum(float(p.get("price", 0)) for p in products)
