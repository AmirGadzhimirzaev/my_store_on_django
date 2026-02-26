from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" c определенными правами'

    def handle(self, *args, **options):
        group, _ = Group.objects.get_or_create(name='Moderators')
        content_type = ContentType.objects.get_for_model(Product)
        permissions = Permission.objects.filter(codename__in=['can_unpublish_product', 'delete_product'], content_type=content_type)
        group.permissions.set(permissions)
        group.save()
