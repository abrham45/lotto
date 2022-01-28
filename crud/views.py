from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import Player
import random
from django.contrib import messages


def index(request):
    player=Player.objects.all()
    return render(request,'index.html',{'player':player})
def createView(request):
    return render(request,'create.html')

def store(request):
    player=Player()
    player.mobile=request.POST.get('mobile')
    player.lot_type=request.POST.get('lot_type')
    player.lot_num=str(player.lot_type)+str(random.randint(0,1000000))
    player.save()
    messages.success(request,"new ticket "+player.lot_num+" for user"+player.mobile+" Added Successfully")
    return redirect('/create')
def viewPlayer(request,pk):
   player = Player.objects.get(id = pk)
   return render(request, 'view.html',{'player':player})
def deletePlayer(request, pk):
    player = Player.objects.get(id = pk)
    player.delete()
    messages.success(request, "player Deleted Successfully")
    return redirect('/')
