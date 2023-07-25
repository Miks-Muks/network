from django.db import models
from django.urls import reverse

from users.models import KaifarikUser


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name chatroom', )
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(KaifarikUser, on_delete=models.CASCADE, related_name='room')

    def get_absolute_url(self):
        return reverse('chat:room', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(KaifarikUser, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
    #
    # def __str__(self):
    #     return self.room
