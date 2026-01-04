from django.db import models

class Blog(models.Model):
    title = models.CharField(
        unique=True,
        verbose_name='Заголовок',
        max_length=100
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name='Содержание'
    )
    photo = models.ImageField(
        upload_to='blog/photos',
        blank=True,
        null=True,
        verbose_name='Фото',
        help_text='Загрузите фото'
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата создания',
        help_text='Укажите кол-во просмотров'
    )
    published = models.BooleanField(
        blank=True,
        null=True,
    )
    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите кол-во просмотров',
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

