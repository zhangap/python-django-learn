from django.db import models


# Create your models here.


class Test(models.Model):
    # 姓名
    name = models.CharField(max_length=500)
    age = models.IntegerField()
