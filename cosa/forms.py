from __future__ import unicode_literals
from django import forms


class CrearCosaForm(forms.Form):
    
    
    cantidad = forms.IntegerField(label="Cantidad", widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "exampleInputAmount", 
        "placeholder": "En Centavos",
        "required": "True"
        }))
    #categoria = forms.ModelChoiceField(queryset=, label=, to_field_name="categoria", attrs={})
    comentario = forms.CharField(label="Comentario", widget=forms.TextInput(attrs={
        "class": "form-control input-padding",
        "id": "exampleInputAmount",
        "placeholder": "Opcional"
        }))