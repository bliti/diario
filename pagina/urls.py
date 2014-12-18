from .views import InicioView


urlpatterns = patterns('',
    (r'^$', InicioView.as_view(), name="inicio")
)