from django.shortcuts import render
from Test.models import *  # Se importan los modelos de la app Test en donde se encuentran Alternativa, Puntaje_usuario y Pregunta

# Vistas cuestionario
# Debería incluir vista respuesta, pregunta, resultados y home. 

def inicio_cuestionario(request):
    return render(request, 'inicio_cuestionario.html')

def casos_2(request):
    return render(request, 'casos_2.html')

