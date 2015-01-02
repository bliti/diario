from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from cosa.models import Cosa
from categoria.models import Categoria
from .forms import NuevaCategoriaForm


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
    
    def get(self, request, *args, **kwargs):
        
        cosas = Cosa.objects.filter(user=self.request.user)
        return render(request, self.template_name, {'cosas': cosas})
    
    #categorias = Categoria.models.filter(user=self.request.user)


"""
class NuevaCategoriaView(TemplateView):
    form_class = NuevaCategoriaForm
    template_name = 'nueva_categoria.html'
    
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': form_class})
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            categoria = Categoria.objects.create(
                categoria=form.cleaned_data['categoria']
                user=self.request.user
                )
           
            return HttpResponseRedirect(reverse_lazy('dashboard'))

        return render(request, self.template_name, {'form': form})


class NuevaCosaView(TemplateView):
    form_class = NuevaCosaForm
    template_name = 'nueva_cosa.html'
"""