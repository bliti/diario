from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import CosaListView
from pagina.views import DeleteCosaView #Note: bring this class over to this file!


urlpatterns = (
    url(r'^$', login_required(CosaListView.as_view()), name='cosas'),
    url(r'^delete/$', login_required(DeleteCosaView.as_view()), name='delete_cosa'),
    )