from tkinter import CASCADE
from django.db import models
from django.conf import settings
from Test.models import *
from Cuestionario.models import *

# Modelo para asociar tiempo de permanencia a usuario

class tiempo(models.Model):
    # Relaciona este modelo con el modelo del usuario. 
    usuario= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tiempo_final= models.DateField(null =True)
