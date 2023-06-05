from django.db import models


# Create your models here.\
class ProductInfo(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default="No description")
    price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
