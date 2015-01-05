from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from pagina.views import DeleteCosaView


urlpatterns = (
    url(r'^delete/$', login_required(DeleteCosaView.as_view()), name='delete_cosa'),
    )