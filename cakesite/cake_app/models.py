from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


class Cake(models.Model):
    name = models.CharField(max_length=50, verbose_name='название', unique=True)
    description = models.TextField(blank=True, null=True,
                                   verbose_name='описание')
    slug = models.SlugField(verbose_name='слаг', unique=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')
    type = models.CharField(max_length=50, choices=[('1', 'торт'), ('2', 'пироженое')], verbose_name='тип')
    techcard = models.JSONField(null=True, blank=True, verbose_name='Техкарта')

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('show_one_cake', kwargs={'slug': self.slug, 'size': 16})

    def save(self):
        super(Cake, self).save()
        if not self.slug:
            self.slug = slugify(translit(f'{self.name} + {self.pk}', 'ru', reversed=True))
            super(Cake, self).save()

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



