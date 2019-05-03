from django.db import models

# Create your models here.


class URL(models.Model):
    url_long = models.URLField(max_length=500, unique=True)
    url_short = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.url_long
