from __future__ import unicode_literals
from django import forms


class CrearCategoriaForm(forms.Form):
    
    
    categoria = forms.CharField(label="Categoria", widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "exampleInputAmount", 
        "placeholder": "Ejemplo: Venta de producto",
        "required": "True"
        }))


class DeleteCategoriaForm(forms.Form):
    
    id = forms.CharField(widget=forms.HiddenInput())
