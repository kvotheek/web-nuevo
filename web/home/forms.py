"""
Opcion para la creación de usuaria distinta a la utilizada en views.py. 
Ambas ocupan auth.models import User, la diferencia es que el otro utiliza user-is_valid para poder luego realizar el post
del usuario a la base de datos.

from django.forms import ModelForm
from Test.models import *
from Cuestionario.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"

"""