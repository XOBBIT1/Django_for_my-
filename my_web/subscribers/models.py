from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Subscriptions(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='profile_user')
    text = models.TextField('Описание')
    image_profile = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.username}: {self.text}"

    class Meta:
        verbose_name = 'Subscriptions'
        verbose_name_plural = 'Subscribers_user'



class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    text = models.TextField('Описание')
    image_profile_user = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.name}: {self.text}"

    class Meta:
        verbose_name = 'Profiles'
        verbose_name_plural = 'Profile_user'
