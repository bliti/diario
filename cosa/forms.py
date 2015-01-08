from __future__ import unicode_literals
from django import forms
from categoria.models import Categoria


class CrearCosaForm(forms.Form):
    
    
    cantidad = forms.IntegerField(label="Cantidad", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "id": "cantidad", 
        "placeholder": "En Centavos",
        "required": "True"
        }))
    
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.none(), widget=forms.Select(attrs={"class": "form-control", "id": "categoria"}))
    
    comentario = forms.CharField(label="Comentario", required=False, widget=forms.TextInput(attrs={
        "class": "form-control input-padding",
        "id": "comentario",
        "placeholder": "Ninguno"
        }))


class DeleteCosaForm(forms.Form):
    
    id = forms.CharField(widget=forms.HiddenInput())