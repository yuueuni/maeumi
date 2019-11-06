from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Label(models.Model):
    id = models.AutoField(primary_key=True)
    label_eng = models.CharField(max_length=50)
    label_kr = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.label_eng
