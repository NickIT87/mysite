from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# SLUG CONSTANTS
# business proposal
_SALE = 'Продажа'
_LEASE = 'Аренда'
_CHANGE = 'Обмен'
_PROP_CHOICES = [(_SALE, 'Продажа'), (_LEASE, 'Aренда'), (_CHANGE, 'Обмен')]


# DB models here.
class Apartment(models.Model):
    # SLUG CONSTANTS
    # bathroom type
    ADJACENT = 'Смежный'
    SEPARATED = 'Раздельный'
    BATHROOM_CHOICE = [(ADJACENT, 'Смежный'), (SEPARATED, 'Раздельный')]
    # window type
    PLASTIC = 'Пластик профиль'
    WOOD = 'Дерево профиль'
    STANDARD = 'Стандартная комплектация'
    WINDOW_CHOICE = [(PLASTIC, 'Пластик профиль'),(WOOD, 'Дерево профиль'),(STANDARD, 'Стандартная комплектация')]
    # balcony type
    OPEN_BALCONY = 'Открытого типа'
    GLAZED_BALCONY = 'Застеклен'
    GLAZED_AND_INSULATED = 'Застеклен и утеплен'
    NO_BALCONY = 'Отсутствует'
    BALCONY_CHOICE = [
        (OPEN_BALCONY, 'Открытого типа'),
        (GLAZED_BALCONY, 'Застеклен'),
        (GLAZED_AND_INSULATED, 'Застеклен и утеплен'),
        (NO_BALCONY, 'Отсутствует')
    ]
    # room condition
    BASIC_REPAIR = 'Базовый ремонт'
    FULL_REPAIR = 'Полный ремонт'
    NO_REPAIR = 'Требуется ремонт'
    ROOM_CONDITION = [(BASIC_REPAIR, 'Базовый ремонт'), (FULL_REPAIR, 'Полный ремонт'), (NO_REPAIR, 'Требуется ремонт')]

    # MODEL FIELDS
    slug_title = 'Apartment'
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    proposal_type = models.CharField(max_length=7, choices=_PROP_CHOICES, default=_SALE, verbose_name='Тип предложения')
    price = models.FloatField(verbose_name='Цена $')
    number_of_rooms = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Кол-во комнат'
    )
    floor_number = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(25)], verbose_name='Этаж'
    )
    total_floors_number = models.PositiveSmallIntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(25)], verbose_name='Всего этажей'
    )
    bathroom = models.CharField(max_length=10, choices=BATHROOM_CHOICE, default=SEPARATED, verbose_name='Туалет')
    window_type = models.CharField(max_length=25, choices=WINDOW_CHOICE, default=PLASTIC, verbose_name='Окна')
    balcony = models.CharField(max_length=20, choices=BALCONY_CHOICE, default=GLAZED_BALCONY, verbose_name='Балкон')
    room_condition = models.CharField(max_length=20, choices=ROOM_CONDITION, default=FULL_REPAIR, verbose_name='Ремонт')
    total_area = models.FloatField(
        default=10.0, validators=[MinValueValidator(10.0), MaxValueValidator(200.0)], verbose_name='Общая площадь кв.м'
    )
    address = models.CharField(max_length=65, verbose_name='Адрес')
    description = models.TextField(blank=True, max_length=400, verbose_name='Описание')

    # METHODS
    # def delete(self):
    #     print("deleted from Class Apartment")

    def __str__(self):
        return  self.slug_title + '_' + self.address


# def get_apartment_dynamic_path_upload_to(instance, filename):
#     #new_filename = '{}.{}'.format(uuid.uuid4, filename.split('.')[-1])
#     return "photos/apartments/{}/{}".format(instance.apartment.id, filename)


class ApartmentGallery(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="apartments/")

    # def delete(self):
    #     self.image.delete()
    #     super().delete()


# my_product = Product()
# my_product.images.all()  где images - related name
# Gallery.objects.filter(product=my_product)
# {{ object.images.all }}    {% for image in object.images.all %}


class House(models.Model):
    # SLUG CONSTANTS
    # window type
    PLASTIC = 'Пластик'
    WOOD = 'Дерево'
    WINDOW_CHOICE = [(PLASTIC, 'Пластик'), (WOOD, 'Дерево')]
    # house condition
    BASIC_REPAIR = 'Базовый ремонт'
    FULL_REPAIR = 'Полный ремонт'
    NO_REPAIR = 'Требуется ремонт'
    HOUSE_CONDITION = [(BASIC_REPAIR, 'Базовый ремонт'), (FULL_REPAIR, 'Полный ремонт'), (NO_REPAIR, 'Требуется ремонт')]
    # residential condition
    RESIDENTIAL = 'Жилой'
    NOT_RESIDENTIAL = 'Не жилой'
    RESIDENTIAL_CONDITION = [(RESIDENTIAL, 'Жилой'), (NOT_RESIDENTIAL, 'Не жилой')]
    # MODEL FIELDS
    slug_title = 'House'
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    proposal_type = models.CharField(max_length=7, choices=_PROP_CHOICES, default=_SALE, verbose_name='Тип предложения')
    price = models.FloatField(verbose_name='Цена $')
    number_of_rooms = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Кол-во комнат'
    )
    total_floors_number = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(25)], verbose_name='Всего этажей'
    )
    window_type = models.CharField(max_length=25, choices=WINDOW_CHOICE, default=PLASTIC, verbose_name='Окна')
    house_condition = models.CharField(
        max_length=20, choices=HOUSE_CONDITION, default=FULL_REPAIR, verbose_name='Ремонт'
    )
    resident_condition = models.CharField(
        max_length=8, choices=RESIDENTIAL_CONDITION, default=RESIDENTIAL, verbose_name='Состояние'
    )
    total_area = models.FloatField(
        default=10.0, validators=[MinValueValidator(10.0), MaxValueValidator(200.0)], verbose_name='Общая площадь кв.м'
    )
    garden_plot_size = models.FloatField(verbose_name='Размер садового участка сот.')
    basement = models.BooleanField(default=True, verbose_name='Подвал?')
    household_buildings = models.BooleanField(default=True, verbose_name='Хоз. постройки?')
    draw_well = models.BooleanField(default=True, verbose_name='Колодец?')
    address = models.CharField(max_length=65, verbose_name='Адрес')
    description = models.TextField(blank=True, max_length=400, verbose_name='Описание')

    def __str__(self):
        return  self.slug_title + '_' + self.address


class HouseGallery(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="houses/")


class LandPlot(models.Model):
    # MODEL FIELDS
    slug_title = 'LandPlot'
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    proposal_type = models.CharField(max_length=7, choices=_PROP_CHOICES, default=_SALE, verbose_name='Тип предложения')
    price = models.FloatField(verbose_name='Цена $')
    size = models.FloatField(verbose_name='Размер земельного участка сот.')
    address = models.CharField(max_length=65, verbose_name='Адрес')
    description = models.TextField(blank=True, max_length=400, verbose_name='Описание')
    image = models.ImageField(upload_to="LandPlots/", blank=True, verbose_name='Фото земельного участка')


class CommercialStructure(models.Model):
    # MODEL FIELDS
    slug_title = 'CommercialStructure'
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    proposal_type = models.CharField(max_length=7, choices=_PROP_CHOICES, default=_SALE, verbose_name='Тип предложения')
    floor_number = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(25)], verbose_name='Этаж'
    )
    total_area = models.FloatField(
        default=30.0, validators=[MinValueValidator(10.0), MaxValueValidator(500.0)], verbose_name='Общая площадь кв.м'
    )
    address = models.CharField(max_length=65, verbose_name='Адрес')
    description = models.TextField(blank=True, max_length=400, verbose_name='Описание')
    image = models.ImageField(upload_to="CommercialStructures/", blank=True, verbose_name='Фото')


class Garage(models.Model):
    # MODEL FIELDS
    slug_title = 'Garage'
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    proposal_type = models.CharField(max_length=7, choices=_PROP_CHOICES, default=_SALE, verbose_name='Тип предложения')
    total_area = models.FloatField(
        default=10.0, validators=[MinValueValidator(3.0), MaxValueValidator(200.0)], verbose_name='Общая площадь кв.м'
    )
    address = models.CharField(max_length=65, verbose_name='Адрес')
    description = models.TextField(blank=True, max_length=400, verbose_name='Описание')
    image = models.ImageField(upload_to="CommercialStructures/", blank=True,  verbose_name='Фото')