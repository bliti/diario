from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import CrearCategoriaForm


class CrearCategoriaView(TemplateView):
    template_name = "crear_categoria.html"
    form_class = CrearCategoriaForm()
    
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})


    def post(self, request, *args, **kwargs): 
        pass   