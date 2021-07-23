from django.contrib import admin
from .models import *


def delete_model(modeladmin, request, queryset):
    print('delete SOMETHINGa')
    print(modeladmin)
    print(request)
    print(queryset)

# Register your models here.
class GalleryInline(admin.TabularInline):
    fk_name = 'apartment'
    model = Gallery


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    actions = [delete_model]

    def delete_queryset(self, request, queryset):
        print('========================delete_queryset========================')
        print(queryset)
        """you can do anything here BEFORE deleting the object(s)"""
        queryset.delete()
        """you can do anything here AFTER deleting the object(s)"""
        print('========================delete_queryset========================')

    def delete_model(self, request, obj):
        print('==========================delete_model==========================')
        print(obj)
        """you can do anything here BEFORE deleting the object"""
        obj.delete()
        """you can do anything here AFTER deleting the object"""
        print('==========================delete_model==========================')

#admin.site.register(Gallery)