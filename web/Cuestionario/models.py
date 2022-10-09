from django.db import models
from Test.models import * # se importa el modelo de preguntas que esta en la aplicacion Test.



class Informacion(models.Model):
    desc= models.CharField(max_length=600)
    url_radiopaedia= models.URLField(blank=True)
    url_SERAM= models.URLField(blank=True)

    respuesta= models.ForeignKey(Alternativa, on_delete=models.CASCADE)

    # retorna un string con metodo f y asi se hace el display de los campos
    # que están dentro del f.
    
    # Esta seccion devuelve lo que se muestra en la pagina de admin
    def __str__(self):
        return f"alternativa:{ self.respuesta.resp}"
    # aqui se llama como diccionario la alternativa y el valor a retornar. 
    # ejemplo, de aqui se llama a la clase alternativa, en donde desde ella misma llamamos a alternativa y al atributo resp. que contiene la respuesta.

    # Se le cambia el nombre a informaciones en el modelo en /admin/
    class Meta:
        verbose_name_plural= "Informaciones"