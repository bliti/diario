from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Categoria(models.Model):
    """
    Categoria de una cosa
    """
    categoria = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    