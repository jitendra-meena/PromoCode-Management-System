from django.urls import path
from authentication.views import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views

urlpatterns = [
    #User's EndPoints
    path('',home,name = 'home'),
    path('userlogin/',userlogin,name = 'userlogin'),
    path('register/',register,name = 'register'),
    path('userdashbord',userdashbord,name = 'userdashbord'),
    path('applycode',applycode,name = 'applycode'),
    path('apply',apply,name = 'apply'),
    path('apply/<int:id>',apply,name = 'apply'),
    path('logout',userlogout,name = 'logout'),




    
]