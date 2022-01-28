from django.db import models

# Create your models here.
class Player(models.Model):

    mobile=models.TextField(max_length=15)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    lot_type=models.CharField(max_length=200)
    lot_num=models.TextField(max_length=200)

