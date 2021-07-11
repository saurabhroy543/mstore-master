from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
