from django.db import models


# Create your models here.\
class ForumMessages(models.Model):
    user = models.TextField()
    content = models.TextField(default="Error in base")
    photo = models.ImageField(upload_to="photos/")
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Сообщения форума"
