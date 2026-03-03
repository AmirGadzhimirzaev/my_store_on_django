from django.core.cache import cache
from unicodedata import category

from catalog.models import Product, Category
from config.settings import CASH_ENABLED


def get_prod_from_cache():
    """Получает данные о продуктах из кеша, если пуст, получают данные из БД"""

    if not CASH_ENABLED:
        return Product.objects.all()

    key = 'prods_list'
    prods = cache.get(key)

    if prods is not None:
        return prods
    prods = Product.objects.all()
    cache.set(key, prods)
    return prods


def get_category_prods_list(category_id):
    return [product.name for product in Product.objects.filter(category_id=category_id)]