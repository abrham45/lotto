from rest_framework import serializers
from .models import Lottery_Player, Video_Uploader,Lottery_Winner, Lottery_Type

class LotteryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery_Type
        fields = '__all__' 

class LotteryPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery_Player
        fields = '__all__' 

class VideoUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_Uploader
        fields = '__all__'  

class LotteryWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lottery_Winner
        fields = '__all__'  