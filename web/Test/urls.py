from django.urls import path
from .views import *

urlpatterns = [
path('', inicio_evaluacion, name='inicio-evaluacion'),
path('casos/<int:pk>/', casos, name='casos'),
]