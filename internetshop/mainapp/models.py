from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField('Название', max_length=60)
    desc = models.TextField('Описание', blank=True)
    # photo = models.ImageField('Фото', upload_to='images/', blank=True)
    year = models.IntegerField('Год выпуска')
    price = models.DecimalField('Цена', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'