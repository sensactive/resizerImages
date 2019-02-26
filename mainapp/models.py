from django.db import models
import requests
import time


# Create your models here.

class Picture(models.Model):
    img = models.ImageField(upload_to='images/', verbose_name='Картинка', null=True, blank=True)
    urlImg = models.URLField(verbose_name='Ссылка на картинку', null=True, blank=True)

    def save(self, *args, **kwargs):
        #Сначала сохраняем
        super().save(*args, **kwargs)
        if self.urlImg:
            # Генерируем имя файла, который создадим по ссылке
            nameOfFile = 'media/images/{}.jpg'.format(time.time())
            # Создаем файл
            with open(nameOfFile, 'wb') as target:
                a = requests.get(self.urlImg)
                target.write(a.content)
            self.img = nameOfFile[6:]
            self.urlImg = None
            self.save()

