from django.shortcuts import render, redirect 
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from .models import UsersPromocode,Promo
from django.shortcuts import render, redirect
import random
from datetime import datetime
import datetime

def home(request):
    if request.user.is_authenticated:
        return redirect('/userdashbord')
       
    return render(request,'users/user-register.html')
def userdashbord(request):
    code = UsersPromocode.objects.filter(user = request.user,promo_code_status = "Active")
    print(code)
    return render(request ,'users/user-dashboard.html',{'code':code })


def register(request):
    if request.method=='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        confirm_password = request.POST.get('confirm_password','')
        user_exs = User.objects.filter(username = username).exists()
        if user_exs:
            return render(request,'users/user-register.html', {'msg': 'Usename already exists'})
        if password == confirm_password:
            user_obj = User.objects.create_user(username =  username, password = password)
        else:
            return render(request,'users/user-register.html', {'msg':'password not matched'})
        return render(request,'users/user-register.html', {'msg':'Successfully registered'})
    else:
        if request.user.is_authenticated:
            return render(request,'users/user-register.html')
        return render(request,'users/user-register.html')
        
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)

            return redirect('/userdashbord')
        else:
            return render(request,'users/user-login.html',{'msg': 'Wrong username or password'})
        return render(request,'users/user-login.html',{'msg': 'Please Register yourself first'})
    else:
        if request.user.is_authenticated:
            return render(request, 'users/user-dashboard.html')
        return render(request,'users/user-login.html')

def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'users/user-register.html')
    else:
       return redirect('/userdashbord')

def get_promo_code(num_chars):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num_chars):
        slice_start = random.randint(0, len(code_chars) - 1)
        code += code_chars[slice_start: slice_start + 1]
    return code




def applycode(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        gender = request.POST.get('gender')
        amount = request.POST.get('amount')
        user = request.user
        start_date = datetime.datetime.now()
        end_date = datetime.date.today() + datetime.timedelta(30)    
        promo_code = Promo.objects.create(code_type = gender,code_name =  get_promo_code(6),start_date = start_date, end_date =end_date )
        promo_code.save()
        code_obj = UsersPromocode.objects.create(user = user,codes = promo_code,birthday = date, gender = gender,order_amount = amount,promo_code_status = "Active"  )
        code_obj.save()
        code = UsersPromocode.objects.filter(user = request.user,promo_code_status = "Active")
        print(code)
        return render(request,'users/user-dashboard.html',{'code':code})

def apply(request,id):
    code_obj = UsersPromocode.objects.get(id = id)
    print(code_obj)
    code_obj.promo_code_status = "Expired"
    code_obj.save()
    print("True")
    code = UsersPromocode.objects.filter(user = request.user, promo_code_status = "Active")
    return render(request,'users/user-dashboard.html',{'code':code})
    




    



