'''
from django.shortcuts import render

# Create your views here.

def player_list(request):
    return render(request, "Lottery_app/player_list.html")

def player_form(request):
    return render(request, "Lottery_app/player_form.html")

def player_delete(request):
    return 
'''

from django.db.models.query import QuerySet
from rest_framework import viewsets
from . import models
from . import serializers
from django.shortcuts import render
import random
from datetime import date

class LotteryTypeView(viewsets.ModelViewSet):
    queryset = models.Lottery_Type.objects.all()
    serializer_class = serializers.LotteryTypeSerializer    

class LotteryPlayerView(viewsets.ModelViewSet):
    queryset = models.Lottery_Player.objects.all()
    serializer_class = serializers.LotteryPlayerSerializer    
    
class VideoUploaderView(viewsets.ModelViewSet):
    queryset = models.Video_Uploader.objects.all()
    serializer_class = serializers.VideoUploaderSerializer

class LotteryWinnerView(viewsets.ModelViewSet):
    queryset = models.Lottery_Winner.objects.all()
    serializer_class = serializers.LotteryWinnerSerializer

def ListPlayers(request):
        obj = models.Lottery_Player.objects.all()
        context = {
            'objects': obj
        }
        return render(request, "Lottery_app/player_list.html",context)

def RandomWinnerPicker(request):
        obj_for_type3 = models.Lottery_Player.objects.filter(purchase_date = date.today(),lottery_type = 3)
        obj_for_type5 = models.Lottery_Player.objects.filter(purchase_date = date.today(),lottery_type = 5)
        obj_for_type10 = models.Lottery_Player.objects.filter(purchase_date = date.today(),lottery_type = 10)
            
            
        context = {}

        if len(obj_for_type3) > 0:  
            context['objects_for_type3'] = random.choice(obj_for_type3)
        if len(obj_for_type5) > 0:  
            context['objects_for_type5'] = random.choice(obj_for_type5)
        if len(obj_for_type10) > 0:   
                context['objects_for_type10'] = random.choice(obj_for_type10)   
        
        return render(request, "Lottery_app/randomize_winner.html",context)


def VideoPlayer(request):
        obj = models.Video_Uploader.objects.all()
        context = {
            'objects': obj
        }
        return render(request, "Lottery_app/video_player.html",context)

   

