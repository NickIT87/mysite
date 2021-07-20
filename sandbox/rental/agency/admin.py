from django.contrib import admin
from .models import *

# Register your models here.
class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]


admin.site.register(Gallery)