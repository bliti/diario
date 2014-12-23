from django.conf.urls import url
from .views import InicioView, EntrarView, DashboardView


urlpatterns = (
    url(r'^$', InicioView.as_view(), name='inicio'),
    url(r'^entrar/$', EntrarView.as_view(), name='entrar'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    )