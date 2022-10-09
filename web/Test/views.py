from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def inicio_evaluacion(request):
    return render(request, 'inicio_evaluacion.html')

"""
def casos(request, pk):
    p=get_object_or_404(Pregunta,pk=pk)
    return render(request, 'casos.html', {'preguntas':p})

    for ans in p.get_respuesta():
        respuestas.append(ans.respuesta)
    preguntas.append({str(p):respuestas})
return JsonResponse({
    'data': preguntas,

})
"""
def casos(request):
    for field in Pregunta._meta.fields:
        print (field.primary_key)
        print (field.name)

    return render(request, 'casos.html')
