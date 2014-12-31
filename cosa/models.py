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
    comentario = models.TextField(null=True)
    categoria = models.ForeignKey(Categoria)
    user = models.ForeignKey(User)
    
    class Meta:
        ordering = ['-pk']
    
    
    def __unicode__(self):
        return self.cantidad
    
    
    def get_absolute_url(self):
        return reverse('cosa-detail', kwargs={'pk': self.pk})