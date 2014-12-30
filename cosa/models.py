from django.db import models
#from django.auth import User
from categoria.models import Categoria


class Cosa(models.Model):
    """
    Define una cosa que se hizo.
    """
    cantidad = models.IntegerField() #todo es en centavos.
    fecha = models.DateTimeFIeld(auto_now_add=True)
    comentario = models.TextField(null=True)
    #categoria = models.ForeignKey('Categoria')
    #user = models.ForeignKey(User)