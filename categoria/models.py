from django.db import models
#from django.auth import User

class Categoria(models.Model):
    """
    Categoria de una cosa
    """
    categoria = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    