from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from .forms import CrearCategoriaForm, DeleteCategoriaForm
from .models import Categoria



class ListaCategoriaView(TemplateView):
    template_name = 'categoria.html'
    form_class = CrearCategoriaForm
    
    def get(self, request, *args, **kwargs):
        categorias = Categoria.objects.filter(user=request.user).order_by('-id')
        return render(request, self.template_name, {'categorias': categorias, 'form': self.form_class})


class CrearCategoriaView(View):
    form_class = CrearCategoriaForm
    
    
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('categorias'))


    def post(self, request, *args, **kwargs): 
        form = self.form_class(request.POST)
        if form.is_valid():
            
            categoria = Categoria.objects.create(
                categoria=form.cleaned_data['categoria'],
                user=self.request.user
                )
            
            return HttpResponseRedirect(reverse_lazy('categorias'))

        return render(request, self.template_name, {'form': form})


class DeleteCategoriaView(View):
    
    
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('categorias'))
    
    def post(self, request, *args, **kwargs):
        form = DeleteCategoriaForm(request.POST)
        if form.is_valid():
            categoria = Categoria.objects.get(id=form.cleaned_data['id'])
            categoria.delete()
            return HttpResponseRedirect(reverse_lazy('categorias'))