from django.urls import path
from .views import *

urlpatterns = [
path('', inicio_cuestionario, name= 'inicio-cuestionario'),
path('<pk>/casos/',casos_2,name='casos-2')
]