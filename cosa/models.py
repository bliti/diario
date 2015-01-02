from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
#from categoria.models import Categoria


class Cosa(models.Model):
    """
    Define una cosa que se hizo.
    """
    cantidad = models.IntegerField() #todo es en centavos.
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(null=True)
    #categoria = models.TextField()
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pk']
    
    
    #def __unicode__(self):
    #    return '{0}{1}'.format(self.categoria, self.cantidad)