from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Название товара"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        blank=True, null=True,
        related_name="catalog"
    )
    price = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Цена за покупку'
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения"
    )
    published = models.BooleanField(
        default=False,
        blank=True,
        null=True,
        verbose_name='Опубликовано'
    )
    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите кол-во просмотров',
        default=0
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Название товара"
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
