from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.TextField('Название')
    text = models.TextField('Описание')
    img = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.title}: {self.text}"

    class Meta:
        verbose_name = 'Пост фото'
        verbose_name_plural = 'Фотки'