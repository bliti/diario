from __future__ import unicode_literals
from django import forms
from categoria.models import Categoria


class CrearCosaForm(forms.Form):
    
    
    cantidad = forms.IntegerField(label="Cantidad", widget=forms.NumberInput(attrs={
        "class": "form-control",
        "id": "exampleInputAmount", 
        "placeholder": "En Centavos",
        "required": "True"
        }))
    
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.none(), widget=forms.Select(attrs={"class": "form-control"}))
    
    comentario = forms.CharField(label="Comentario", widget=forms.TextInput(attrs={
        "class": "form-control input-padding",
        "id": "exampleInputAmount",
        "placeholder": "Opcional"
        }))