from django.core.cache import cache

from catalog.models import Product
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
