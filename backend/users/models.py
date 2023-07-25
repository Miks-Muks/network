from django.db import models
from sorl.thumbnail import ImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Create your models here.


class KaifarikUser(AbstractUser):
    verify = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(KaifarikUser, on_delete=models.CASCADE, related_name='user_profile')
    photo = ImageField(upload_to='users/profile', verbose_name='Photo profile', default='profile/default.jpg')
    about = models.TextField(verbose_name='About user', help_text='awdawd', blank=True, null=True,
                             default='Последователь')
    city = models.CharField(max_length=50, default='Kaif')

    def __str__(self):
        return self.user.username


class Role(models.Model):
    name = models.CharField(max_length=70, verbose_name='Роль пользователя')
    user = models.ForeignKey(KaifarikUser, on_delete=models.CASCADE, verbose_name='Связанный пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class Speciality(models.Model):
    user = models.ForeignKey(KaifarikUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Специальность')

    def __str__(self):
        return f'{self.name} of {self.user}'

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class AddedPhoto(models.Model):
    user = models.ForeignKey(KaifarikUser, on_delete=models.CASCADE)
    image = models.ImageField('users/photo_users')
    description = models.CharField(max_length=100, verbose_name='Описание к фотке')

    def __str__(self):
        return self.description


class LinksProfile(models.Model):
    user = models.ForeignKey(KaifarikUser, on_delete=models.CASCADE)
    link = models.URLField(verbose_name='Cсылки на страницы', max_length=300)

    def __str__(self):
        return f'{self.link} пользователя {self.user.name}'
