from django.db import models


# Create your models here.
class Member(models.Model):
    member_id = models.CharField(max_length=20)
    member_name = models.CharField(max_length=20)

    def __str__(self):
        return self.member_name

    def __str__(self):
        return self.member_id
