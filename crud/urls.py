from django.conf.urls import url
from django.urls import path
from .views import createView,store,index,viewPlayer,deletePlayer
urlpatterns = [
    path('create',createView,name="create"),
    path('store', store, name='store'),
    path('', index),
    path('view/<int:pk>', viewPlayer, name='viewPlayer'),
    path('delete/<int:pk>', deletePlayer, name='deletePlayer'),
    # path('update/<int:pk>', updateView, name='updateEmp'),
    # path('edit/<int:pk>', update, name='edit'),

]