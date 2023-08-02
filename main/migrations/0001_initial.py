# Generated by Django 4.2 on 2023-07-30 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Описание')),
                ('img', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.categories')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tovara', models.CharField(db_index=True, max_length=10, unique=True)),
                ('amount_of_items', models.CharField(db_index=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Товары корзины',
                'ordering': ['id'],
            },
        ),
    ]
