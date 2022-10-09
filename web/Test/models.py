from django.db import models
from django.contrib.auth.models import User  
# el modelo anterior es un modelo de usuario y contraseña que viene por defecto en Django. Está compuesto de un identificador de usuario y contraseña. Sirve para tener la autenticación 

"""
 Se crea el modelo en donde se obtendrá 4 bloques:
- Bloque de preguntas
- Bloque de respuestas
- Bloque de información sobre las respuestas (en seccion cuestionario)
- Bloque de respuestas almacenadas del usuario
"""

class Pregunta(models.Model):
    img_patologia= models.ImageField(upload_to='radiopaedia/imgs/', blank=True)
    contenido= models.CharField(max_length= 200)

    # Devuelve lo contenido dentro de la variable contenido en formato string
    def __str__(self):
        return str(self.contenido)

    # Relaciona la clase de preguntas con el modelo de respuestas
    # se llama relacion inversa
    def get_respuesta(self):
        return self.respuesta.all()


class Alternativa(models.Model):
    respuesta= models.CharField(max_length=600, blank=True)
    respuesta_correcta= models.BooleanField(default=False) # crea una casilla para poder marcar si la respuesta es correcta o no
    pregunta= models.ForeignKey(Pregunta, on_delete= models.CASCADE, related_name='respuesta') 
    
    """ 
    Esto va a permitir eliminar una respuesta y que ésta esté relacionada con la pregunta y por tanto al eliminar una se elimina la siguiente. 
    Además related_name=respuesta permite relacionar esta clase con las preguntas. 
    puede ser utilizando related_name="wtf" y ocupando self.wtf.all() ó sin related name
    sería self.nombremodeloenminuscula_set.all()

    """
    # Retorna este tipo de escritura en el panel de administracion al entrar a los modelos
    def __str__(self):
        return f"pregunta: {self.pregunta.contenido}, alternativa: {self.respuesta}, correcta: {self.respuesta_correcta}"

    # Se reazlia la relacion inversa con la clase de informacion. 
    def get_info(self):
        return self.informacion_set.all()

# esta seccion debería almacenar las preguntas y sus respuestas y tengo que ver como hacer para que luego eso se almacene como estadistica. 
class Puntaje_usuario(models.Model):
    resp= models.ForeignKey(Alternativa, on_delete=models.CASCADE, null=True)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    ptje= models.FloatField()
    fecha= models.DateTimeField(auto_now_add=True) # asi se puede saber la fecha en la cual realizó el test/cuestionario/ etc


""" por ahora lo que entiendo es que retorna las preguntas y sus respectivas respuestas correctas/incorrectas
Aqui se relaciona el usuario y las preguntas contestadas (en los otros aparece quiz xd. ) 
TODAVIA NO SÉ COMO RELACIONAR O ALMACENAR LA PREGUNTA SELECCIONADA PERO 
SE DEBERÍA HACER CON UN METODO POST EN EL PUNTAJE
ADEMÁS DEBERÍA HABER UNA TABLA DENTRO DE LA TABLA
O QUE LA TABLA TENGA COLUMNA DE NUMEROS DE LAS PREGUNTAS en las que se equivocó (puede ser la pk)
y columna de numeros de preguntas acertadas
ademas tener columna que contabilice en cuantas se equivoco y en cuantas acertó 
"""


    
