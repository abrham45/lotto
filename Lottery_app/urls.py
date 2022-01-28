'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list),
    path('list/', views.player_form)
]
'''

from Lottery_app.views import LotteryPlayerView, VideoUploaderView,LotteryWinnerView,LotteryTypeView
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Lottery_Type', LotteryTypeView)
router.register('Lottery_Player', LotteryPlayerView)
router.register('Video_Uploader', VideoUploaderView)
router.register('Lottery_Winner', LotteryWinnerView)



urlpatterns = [
    path('', include(router.urls))

]