from django.urls import path
from .views import *

urlpatterns= [

    path('', home, name="home"),

    # url del registro, login y logout de la página.
    path("signup/", Signup, name="signup"),
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),


]