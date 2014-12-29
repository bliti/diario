from django.conf.urls import url
from .views import InicioView, DashboardView


urlpatterns = (
    url(r'^$', InicioView.as_view(), name='index'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    )