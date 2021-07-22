from django.db import models
from django_matplotlib import MatplotlibFigureField


class Home(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='static/media', null=True)

    def __str__(self):
        return self.title






