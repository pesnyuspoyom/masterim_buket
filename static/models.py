from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField('Название продукта', max_length=100, unique=True)
    description = models.TextField('Описание продукта')
    image = models.ImageField('Фото продукта', upload_to='products/')
    video = models.FileField('Видео продукта', upload_to='videos/', null=True, blank=True)
    available = models.BooleanField('Актуален или нет', default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
