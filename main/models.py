from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Items(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    content = models.TextField(verbose_name='Описание')
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT)
    img = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.CharField(max_length=20, verbose_name='Цена')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_slug': self.slug})
    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Categories(models.Model):
    category = models.CharField(max_length=100, db_index=True)
    #slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.category
    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'cat_slug': self.slug})
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']



class Basket(models.Model):
    id_tovara = models.CharField(max_length=10, db_index=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_of_items = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.id_tovara
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Товары корзины'
        ordering = ['id']
