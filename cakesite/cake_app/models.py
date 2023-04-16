from django.db import models
from django.urls import reverse


class Cake(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', unique=True)
    description = models.TextField(blank=True, null=True,
                                   verbose_name='описание')
    slug = models.SlugField(verbose_name='слаг', unique=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')
    type = models.CharField(max_length=50, choices=[('1', 'торт'), ('2', 'пироженое')], verbose_name='тип')

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('show_one_cake', kwargs={'slug': self.slug, 'size': 16})

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', unique=True)
    price = models.FloatField(verbose_name='цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class TechCard(models.Model):
    model_cake = models.ForeignKey(Cake, on_delete=models.SET_NULL, null=True,
                                   verbose_name='торт', related_name='techcards')
    model_product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                      null=True,
                                      verbose_name='продукт', related_name='techcards')
    quantity = models.FloatField(verbose_name='количество')

    class Meta:
        verbose_name = 'Тех-карта'
        verbose_name_plural = 'Тех-карты'
        ordering = ['model_cake']

    def __str__(self):
        return f'{self.model_cake} - {self.model_product}'
