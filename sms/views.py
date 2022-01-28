import random
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.timezone import make_aware
from django.views.decorators.csrf import csrf_exempt

import africastalking
from django.views.decorators.http import require_POST

from sms.models import Outbox
from crud.models import  Player
from random import randint



@csrf_exempt
@require_POST
def incoming_message(request):
    text = request.POST.get('text')
    text=str(text).strip()
    player_number=request.POST.get('from')
    print(text,player_number)
    if text=="play":
        Outbox.send(player_number, "1. 3 birr lottery\n 2.5 birr lottery\n 3.10 birr lottery\n 4.20 birr lottery")
    elif text=="1":
        generate_lot(request,player_number,3)
    elif text=="2":
        generate_lot(request,player_number,5)
    elif text=="3":
        generate_lot(request,player_number,10)
    elif text=="4":
        generate_lot(request,player_number,20)
    else:
        Outbox.send(player_number,"incorrect input  please try again")
    return HttpResponse(status=200)

def  generate_lot(request,player_number,type):
        player = Player()
        player.mobile = player_number
        player.lot_type = str(type)
        range_start = 10**(9)
        range_end = (10**10)-1
        player.lot_num = player.lot_type + str(randint(range_start, range_end))
        check_num=Player.objects.all()
        print(check_num)
        current_lot_nums=[]
        for lottery in check_num:
            current_lot_nums.append(int(lottery.lot_num))
        print(current_lot_nums)
        if int(player.lot_num) not in current_lot_nums:
            print(f"True{lottery.lot_num}")
            player.save()
            Outbox.send(player_number,
                        f"your lottery number is {player.lot_num }")
            current_lot_nums.clear()     
        else:
            print("didn't found i'm gonna try again")
            print(current_lot_nums)
            incoming_message(request)