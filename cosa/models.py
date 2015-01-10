from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from categoria.models import Categoria


class Cosa(models.Model):
    """
    Define una cosa que se hizo.
    """
    cantidad = models.IntegerField() #todo es en centavos.
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()
    categoria = models.TextField()
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pk']
    
    
    def __unicode__(self):
        return self.cantidad


class SumarCantidad(object):
    """
    Takes in a Cosa queryset
    and sum the cantidad field
    to return a total.
    """
    
    def __init__(self, cosas):
        """
        cosas queryset = Cosa Objects.
        """
        self.total = sum([cosa.cantidad for cosa in cosas])
        