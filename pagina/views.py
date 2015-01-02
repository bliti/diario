from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from cosa.models import Cosa
from categoria.models import Categoria
from cosa.forms import CrearCosaForm


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(TemplateView):
    template_name = 'dashboard_main.html'
    form_class = CrearCosaForm()
    
    def get(self, request, *args, **kwargs):
        self.form_class.fields['categoria'].queryset = Categoria.objects.filter(user=request.user) 
        cosas = Cosa.objects.filter(user=self.request.user)
        return render(request, self.template_name, {'cosas': cosas, 'form': self.form_class})
    
    
    def post(self, request, *args, **kwargs):
        pass