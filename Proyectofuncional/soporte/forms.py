from django import forms

class FormularioContacto(forms.Form):

    asunto=forms.CharField(max_length=50, required=True)
    mensaje=forms.CharField(widget=forms.Textarea(attrs={"rows":7, "cols":24}), max_length=300, required=True)
