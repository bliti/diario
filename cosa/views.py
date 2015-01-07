from django.views.generic.list import ListView
from .models import Cosa


class CosaListView(ListView):
    """
    Todas las cosas del usuario. Paginadas bien bonitas.
    """
    model = Cosa
    template_name = 'cosa_list.html'
    paginate_by = 25
    context_object_name = 'cosas'
    
    
    def get_queryset(self):
        return Cosa.objects.filter(user=self.request.user)