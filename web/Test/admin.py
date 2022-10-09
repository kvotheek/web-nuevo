from django.contrib import admin
from .models import *

# Se registran los modelos

# Hacer la prueba de comentar la clase alternativainline
# ver cual es el cambio si se registra normal
class AlternativaInline(admin.TabularInline):
    model= Alternativa

class PreguntaAdmin(admin.ModelAdmin):
    inlines=[AlternativaInline]

admin.site.register(Pregunta, PreguntaAdmin) 
admin.site.register(Alternativa)

admin.site.register(Puntaje_usuario)