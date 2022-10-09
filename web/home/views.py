from datetime import datetime

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.contrib import messages
# https://stackoverflow.com/questions/67721582/django-get-last-login-time-of-1-user-and-list-of-all-user
# https://docs.djangoproject.com/en/4.1/_modules/django/contrib/messages/api/

from .models import *



def home(request):
    return render (request, 'home.html')

# Esta parte realiza el registro y utiliza la funcion user.is_authenticated
def Signup(request):
    if request.user.is_authenticated:
        return redirect('/home')  
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        nombre=request.POST['nombre']
        apellidos=request.POST['apellido']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        
        if password != confirm_password:
            return redirect('/')
     # Dentro del modelo auth_user incluido en django se encuentran las variables first_name y last_name, por tanto se utiliza user.atributo 
        user = User.objects.create_user(username, email, password)
        user.first_name = nombre
        user.last_name = apellidos
        user.save()
        return render(request, 'login.html')  
    return render(request, "signup.html")

# Funcion que realiza el inicio de sesion 
def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html") 
            #messages.info(request, 'Username OR password is incorrect')

    return render(request, "login.html")

# Funcion que realiza el cierre de sesion
def Logout(request):
    # Se calcula que estuvo la persona antes de cerrar sesion por voluntad propia
    #tiempo_f= datetime.now()
    tiempo_inicio= request.user.last_login
    #tiempo_final= tiempo_inicio-1

    usuario = request.user

    tiempo.objects.create(tiempo_final=tiempo_inicio, usuario=usuario)

    logout(request)
    return redirect('/')



"""
# Permite almacenar el tiempo de permanencia del usuario
def tiempo_permanencia(request):
    if request.user.is_authenticated:
"""