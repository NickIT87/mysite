from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# DB models here.
class Apartment(models.Model):
    # SLUG CONSTANTS
    # business proposal
    SALE = 'Продажа'
    LEASE = 'Аренда'
    CHANGE = 'Обмен'
    PROP_CHOICES = [(SALE, 'Продажа'), (LEASE, 'Aренда'), (CHANGE, 'Обмен')]
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
    slug_title = 'Flat'
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    proposal_type = models.CharField(max_length=7, choices=PROP_CHOICES, default=SALE, verbose_name='Тип предложения')
    price = models.FloatField(verbose_name='Цена $')
    number_of_rooms = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Кол-во комнат'
    )
    floor_number = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(25)], verbose_name='Этаж'
    )
    total_floor_number = models.PositiveSmallIntegerField(
        default=10, validators=[MinValueValidator(1), MaxValueValidator(25)], verbose_name='Всего этажей'
    )
    bathroom = models.CharField(max_length=10, choices=BATHROOM_CHOICE, default=SEPARATED, verbose_name='Туалет')
    window_type = models.CharField(max_length=25, choices=WINDOW_CHOICE, default=PLASTIC, verbose_name='Окна')
    balcony = models.CharField(max_length=20, choices=BALCONY_CHOICE, default=GLAZED_BALCONY, verbose_name='Балкон')
    room_condition = models.CharField(max_length=20, choices=ROOM_CONDITION, default=FULL_REPAIR, verbose_name='Ремонт')
    total_area = models.FloatField(
        default=10.0, validators=[MinValueValidator(10.0), MaxValueValidator(200.0)], verbose_name='Общая площадь кв.м'
    )
    address = models.CharField(max_length=250, verbose_name='Адрес')
    description = models.TextField(blank=True, verbose_name='Описание')

    # METHODS
    # def delete(self):
    #     print("deleted from Class Apartment")

    def __str__(self):
        return  self.slug_title


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