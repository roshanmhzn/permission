from django.conf import settings
from django.urls import reverse
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

    class Meta:
        permissions = (('can_make_flutter_effect', 'Can make flutter effect'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
