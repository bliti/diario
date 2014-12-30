from __future__ import unicode_literals
from django import forms
from registration.forms import RegistrationForm


class RegistrationFormSpanish(RegistrationForm):
    
    
    def __init__(self, *args, **kwargs):
        super(RegistrationFormSpanish, self).__init__(*args, **kwargs):
        self.fields['username'].label = "Usuario"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Contraseña (De Nuevo)"