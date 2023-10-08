from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse, reverse_lazy

@login_required(login_url=reverse_lazy('login'))
def profile(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    redirect_url=reverse('profile')
    if request.method=="GET":
        if request.user.is_authenticated: # если полльзователь зарегистрирован, то его редиректит (переносит) на страничку профиля, если нет, на страничку регистрации
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username'] # из поступившего запроса смотрим атрибут пост, ключ username
    password = request.POST['password'] # все , что пользователь вводит в полях, будет записываться в переменные 
    user = authenticate(request, username=username, password=password) # возвращает пользователя, если он есть 
    if user is not None: # а если он найден
        login(request, user) # проводим авторизацию
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error": "Пользователь не найдён"})

def logout_view(request):
    logout(request) # выходим
    return redirect(reverse('login'))

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user=user)
            return redirect(reverse('profile'))
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'app_auth/register.html', context)