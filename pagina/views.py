from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from datetime import datetime
from cosa.models import Cosa
from categoria.models import Categoria
from cosa.forms import CrearCosaForm, DeleteCosaForm


class IndexView(TemplateView):
    template_name = 'index.html'


class DashboardView(TemplateView):
    template_name = 'dashboard_main.html'
    form_class = CrearCosaForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        form.fields['categoria'].queryset = Categoria.objects.filter(user=request.user) 
        
        return render(request, self.template_name, {
            'cosas': Cosa.objects.filter(user=self.request.user)[:25],
            'form': form,
            'fecha_de_hoy': datetime.today().date()
            })
    
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.fields['categoria'].queryset = Categoria.objects.filter(user=request.user)
        if form.is_valid():
            
            cosa = Cosa.objects.create(
                cantidad=form.cleaned_data['cantidad'],
                comentario=form.cleaned_data['comentario'],
                categoria=form.cleaned_data['categoria'],
                user=self.request.user
                )
            
            return HttpResponseRedirect(reverse_lazy('dashboard'))

        return render(request, self.template_name, {
            'cosas': Cosa.objects.filter(user=self.request.user)[:25],
            'form': form,
            'fecha_de_hoy': datetime.today().date()
            })


class DeleteCosaView(View):
    
    
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('dashboard'))
    
    def post(self, request, *args, **kwargs):
        form = DeleteCosaForm(request.POST)
        if form.is_valid():
            cosa = Cosa.objects.get(id=form.cleaned_data['id'])
            cosa.delete()
            return HttpResponseRedirect(reverse_lazy('dashboard'))
        
        