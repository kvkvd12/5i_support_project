from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import get_user_model
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else:
            return render(request, 'user/signup.html')
    
    if request.method == 'POST':
        team_name = request.POST.get('team_name','')
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        
        if password != password2:
            return render(request, 'user/signup.html',{'error':'패스워드를 확인 해 주세요!'})
        else:
            if username == '' or password == '' or team_name == "":
                return render(request, 'user/signup.html',{'error':'빈칸을 모두 채워주세요!'})
            
            exist_user = get_user_model().objects.filter(username=username)   
            if exist_user:
                return render(request, 'user/signup.html',{'error':'사용자가 존재합니다!'})
            else:
                User.objects.create_user(team_name=team_name, username=username, password=password)
                return redirect('/login')
            
def login(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else:
            return render(request, 'user/login.html')
        
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/home')
        else:
            return render(request,'user/login.html',{'error':'유저이름 혹은 패스워드를 확인 해 주세요'})
    

    