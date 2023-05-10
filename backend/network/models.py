from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from .validators import check_mate


class TopicKaif(models.Model):
    title = models.CharField(verbose_name='Тема кайфа', max_length=40, blank=False, unique=True)
    info = models.TextField(verbose_name='Суть темы', null=True)
    photo = models.ImageField(upload_to='network/topic')
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)

    def get_absolute_url(self):
        return reverse("network:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class CommentTopic(models.Model):
    topic = models.ForeignKey(TopicKaif, on_delete=models.CASCADE, related_name='comment_topic')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)
    comment = models.CharField(max_length=100, verbose_name='Comment', validators=[check_mate])

    def __str__(self):
        return self.comment
