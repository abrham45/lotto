from django.urls import path
from django.urls.resolvers import URLPattern
from sms import views

urlpatterns =[
    path('',views.incoming_message,name="sms")
]
