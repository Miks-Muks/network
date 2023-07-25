from django.db import models
from django.urls import reverse

from .validators import check_mate
from users.models import KaifarikUser


class TopicKaif(models.Model):
    title = models.CharField(verbose_name='Тема кайфа', max_length=40, blank=False, unique=True)
    info = models.TextField(verbose_name='Суть темы', null=True)
    photo = models.ImageField(upload_to='network/topic')
    user = models.ForeignKey(KaifarikUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("network:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class CommentTopic(models.Model):
    topic = models.ForeignKey(TopicKaif, on_delete=models.CASCADE, related_name='comment_topic')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(KaifarikUser, related_name='user_comments', null=True, blank=True)
    comment = models.CharField(max_length=100, verbose_name='Comment', validators=[check_mate])

    def __str__(self):
        return self.comment
