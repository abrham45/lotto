from django.db import models

# Create your models here.

class Lottery_Type(models.Model):   
     type = models.IntegerField()

class Lottery_Player(models.Model):
    
     phone_number = models.CharField(max_length=13)
     lottery_type = models.ForeignKey(Lottery_Type, default=None, on_delete=models.CASCADE)
     purchase_date = models.DateField()
     purchase_time = models.TimeField()
     lottery_number = models.CharField(max_length=20)

class Video_Uploader(models.Model):
    
     uploader_name = models.CharField(max_length=50)
     uploader_phone_number = models.CharField(max_length=13) 
     winner_phone_number = models.ForeignKey(Lottery_Player, default=None, on_delete=models.CASCADE)
     video_url = models.FileField(upload_to="Videos")
     
class Lottery_Winner(models.Model):   
     winner = models.ForeignKey(Lottery_Player, default=None, on_delete=models.CASCADE)
    