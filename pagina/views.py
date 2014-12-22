from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse_lazy
from .forms import EntrarForm


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
    
    
    def get(self, request, *args, **kwargs):
        """
        show the login form
        """
        return render(self.request, 'entrar.html', {"form": EntrarForm()})


    def post(self, request, *args, **kwargs):
        """
        check if login is successful and redir to dashboard if
        else show the form again
        """
        pass

