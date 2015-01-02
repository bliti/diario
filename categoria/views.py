from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from .forms import CrearCategoriaForm
from .models import Categoria


class CrearCategoriaView(TemplateView):
    template_name = "crear_categoria.html"
    form_class = CrearCategoriaForm
    
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})


    def post(self, request, *args, **kwargs): 
        form = self.form_class(request.POST)
        if form.is_valid():
            
            categoria = Categoria.objects.create(
                categoria=form.cleaned_data['categoria'],
                user=self.request.user
                )
            
            return HttpResponseRedirect(reverse_lazy('dashboard'))

        return render(request, self.template_name, {'form': form}) 