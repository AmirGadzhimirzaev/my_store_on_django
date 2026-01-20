from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test catalog"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Продукты питания',
                                           description='Набор продуктов, которые имеют схожие питательные свойства и имеют схожие способы получения их в природе')

        products = [
            {'name': 'Молоко 1%', 'description': 'Молоко с низким процентом жирности', 'category': category,
             'price': '120', 'created_at': '2025-12-27'},
            {'name': 'Нарезной батон', 'description': 'Свежий хлеб', 'category': category, 'price': '120',
             'created_at': '2025-12-27'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product exist: {product.name}'))
