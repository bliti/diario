from django import forms


class CrearCosaForm(forms.Form):
    
    
    cantidad = forms.IntegerField(label="Cantidad", attrs={})
    categoria = forms.ModelChoiceField(queryset=, label=, to_field_name="categoria", attrs={})
    comentario = forms.CharField(label="Comentario", attrs={})