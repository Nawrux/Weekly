from django.db import models

# Create your models here.


class week(models.Model):
    # id = models.AutoField(primary_key=True)
    weekday = models.TextField()
    event = models.TextField()