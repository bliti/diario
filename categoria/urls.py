from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import CrearCategoriaView


urlpatterns = (
    url(r'^crear/$', login_required(CrearCategoriaView.as_view()), name='crear_categoria'),
    )