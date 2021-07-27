# Generated by Django 3.2.3 on 2021-07-27 13:15

import agency.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('proposal_type', models.CharField(choices=[('Продажа', 'Продажа'), ('Аренда', 'Aренда'), ('Обмен', 'Обмен')], default='Продажа', max_length=7, verbose_name='Тип предложения')),
                ('price', models.FloatField(verbose_name='Цена $')),
                ('number_of_rooms', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Кол-во комнат')),
                ('floor_number', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(25)], verbose_name='Этаж')),
                ('total_floor_number', models.PositiveSmallIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(25)], verbose_name='Всего этажей')),
                ('bathroom', models.CharField(choices=[('Смежный', 'Смежный'), ('Раздельный', 'Раздельный')], default='Раздельный', max_length=10, verbose_name='Туалет')),
                ('window_type', models.CharField(choices=[('Пластик профиль', 'Пластик профиль'), ('Дерево профиль', 'Дерево профиль'), ('Стандартная комплектация', 'Стандартная комплектация')], default='Пластик профиль', max_length=25, verbose_name='Окна')),
                ('balcony', models.CharField(choices=[('Открытого типа', 'Открытого типа'), ('Застеклен', 'Застеклен'), ('Застеклен и утеплен', 'Застеклен и утеплен'), ('Отсутствует', 'Отсутствует')], default='Застеклен', max_length=20, verbose_name='Балкон')),
                ('room_condition', models.CharField(choices=[('Базовый ремонт', 'Базовый ремонт'), ('Полный ремонт', 'Полный ремонт'), ('Требуется ремонт', 'Требуется ремонт')], default='Полный ремонт', max_length=20, verbose_name='Ремонт')),
                ('total_area', models.FloatField(default=10.0, validators=[django.core.validators.MinValueValidator(10.0), django.core.validators.MaxValueValidator(200.0)], verbose_name='Общая площадь кв.м')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=agency.models.get_apartment_dynamic_path_upload_to)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='agency.apartment')),
            ],
        ),
    ]
