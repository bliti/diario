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
    form_class = CrearCosaForm
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        form.fields['categoria'].queryset = Categoria.objects.filter(user=request.user) 
        cosas = Cosa.objects.filter(user=self.request.user)[:25]
        return render(request, self.template_name, {'cosas': cosas, 'form': form})
    
    
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

        return render(request, self.template_name, {'form': form})