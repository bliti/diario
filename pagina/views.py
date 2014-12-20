from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse_lazy


class InicioView(TemplateView):


    def get(self, request, *args, **kwargs):
        """
        check if user is logged in to redirect to 
        dashboard
        """
        if request.user.is_authenticated():
            return redirect(reverse_lazy('entrar'))
        
        return render(self.request, 'inicio.html')


class EntrarView(TemplateView):
    template_name = 'entrar.html'