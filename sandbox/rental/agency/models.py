from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField()


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def delete(self):
        self.image.delete()
        super().delete()