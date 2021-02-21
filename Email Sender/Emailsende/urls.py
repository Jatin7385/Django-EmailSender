from django.urls import path

from . import views

urlpatterns = [
    path('',views.sendemail,name = 'sendemail'),
    path('sendmail',views.sendmail,name='sendmail'),
    
]