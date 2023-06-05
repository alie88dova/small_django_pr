from django.db import models

# Create your models here.

class OurUser(models.Model):
    user = models.TextField()
    auth = models.BooleanField()

    class Meta:
        verbose_name = "Подключенные пользователи"
