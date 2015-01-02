from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import IndexView, DashboardView


urlpatterns = (
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^dashboard/$', login_required(DashboardView.as_view()), name='dashboard'),
    )