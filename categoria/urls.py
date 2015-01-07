from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import CrearCategoriaView, ListaCategoriaView, DeleteCategoriaView


urlpatterns = (
    url(r'^$', login_required(ListaCategoriaView.as_view()), name='categorias'),    
    url(r'^crear/$', login_required(CrearCategoriaView.as_view()), name='crear_categoria'),
    url(r'^borrar/$', login_required(DeleteCategoriaView.as_view()), name='borrar_categoria'),    
        
    )