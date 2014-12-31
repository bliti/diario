from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import Cosa


class CosaCreate(CreateView):
    model = Cosa
    fields = ['cantidad', 'comentario', 'categoria']
    
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CosaCreate, self).form_valid(form)


class CosaDetail(DetailView):
    model = Cosa