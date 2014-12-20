from django.conf.urls import url
from .views import InicioView, EntrarView


urlpatterns = (
    url(r'^$', InicioView.as_view(), name='inicio'),
    url(r'^/entrar$', EntrarView.as_view(), name='entrar'),
    )