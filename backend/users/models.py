from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.urls import reverse


# Create your models here.
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = ImageField(upload_to='users/profile', verbose_name='Photo profile', default='profile/default.jpg')
    about = models.TextField(verbose_name='About user', help_text='awdawd', blank=True, null=True,
                             default='Последователь')
    city = models.CharField(max_length=50, default='Kaif')

    def __str__(self):
        return self.user.username


class AddedPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('users/photo_users')
    description = models.CharField(max_length=100, verbose_name='Описание к фотке')

    def __str__(self):
        return self.description


class LinksProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(verbose_name='Cсылки на страницы', max_length=300)

    def __str__(self):
        return f'{self.link} пользователя {self.user.name}'
