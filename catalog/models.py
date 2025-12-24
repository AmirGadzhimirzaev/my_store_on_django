from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Название товара")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="catalog/photo", blank=True, null=True, verbose_name="Фото")
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, verbose_name="Категория", blank=True, null=True, related_name="products"
    )
    purchase_price = models.IntegerField()
    created_at = models.DateField(blank=True, verbose_name="Дата создания")
    updated_at = models.DateField(blank=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Название товара")
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
