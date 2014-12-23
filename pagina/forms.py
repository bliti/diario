# -*- coding: utf-8 -*-
from django import forms

class EntrarForm(forms.Form):
    email = forms.CharField(label='Correo Electrónico', widget=forms.TextInput(attrs={
        'required': 'True',
        'class': 'form-control',
        'type': 'email',
        'placeholder': 'Correo Electrónico',
        'autofocus': 'True'
        }))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'required': 'True',
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Contraseña',
    }))
