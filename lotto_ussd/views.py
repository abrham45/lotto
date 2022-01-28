from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

from time import gmtime, strftime
showtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
import sys
import random
from crud.models import Player
import sys
import random

import africastalking
from django.http import HttpResponse
# TODO: Initialize Africa's Talking
# print key_num.random() #produces a number between 0 and 1
# print


@csrf_exempt
def ussd(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        response = ""
        if text == "":
            response = "CON Welcome To Online Lottery service Please choose your option  \n"

            response += "1. 3  Birr Lottery \n"
            response += "2. 5  Birr Lottery \n"
            response += "3. 10 Birr Lottery \n"
            response += "4. 20 Birr Lottery \n"

        elif text == "1":
            player = Player()
            player.mobile = phone_number
            player.lot_type=str(3)
            # lis = []
            # while len(lis) < 5:
            #     # This checks to see if there are duplicate numbers
            #     r = random.randint(1, 9)
            #     if r not in lis:
            #         lis.append(r)
            player.lot_num = str(3) + str(random.randint(0, 1000000))
            player.save()
            response = "END Your Phone Number is {0} \n you Lottery Number is {1}".format(phone_number,  player.lot_num ),
            message(phone_number,player.lot_num)


        elif text == "2":

            player = Player()
            player.mobile = phone_number
            player.lot_type = str(5)
            player.lot_num = str(5) + str(random.randint(0, 1000000))
            player.save()
            response = "END Your Phone Number is {0} \n you Lottery Number is {1}".format(phone_number, player.lot_num),
            message(phone_number, player.lot_num)
        elif text == "3":

            player = Player()
            player.mobile = phone_number
            player.lot_type = str(10)
            player.lot_num = str(10) + str(random.randint(0, 1000000))
            player.save()
            response = "END Your Phone Number is {0} \n you Lottery Number is {1}".format(phone_number, player.lot_num),
            message(phone_number, player.lot_num)

        elif text == "4":

            player = Player()
            player.mobile = phone_number
            player.lot_type = str(20)
            player.lot_num = str(20) + str(random.randint(0, 1000000))
            player.save()
            response = "END Your Phone Number is {0} \n you Lottery Number is {1}".format(phone_number, player.lot_num)
            message(phone_number, player.lot_num)
        else:
            response = "END incorrect"
        return HttpResponse(response)



def message(phone,lot_num):
        username = 'sandbox'
        api_key = '413952d3ed46f0e66e312d04221ca3308a5c4c5d9464d5d959343ae4abd33327'
        africastalking.initialize(username, api_key)
        sms = africastalking.SMS
        # Set the numbers in international format
        recipients = [phone]
        # Set your message
        message = "your Lottery number is {0}".format(lot_num)
        # Set your shortCode or senderId
        sender = "lotto"
        try:
            response = sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')




