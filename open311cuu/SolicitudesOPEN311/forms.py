from django import forms
from .models import SolicitudesOPEN311

class SolicitudesOPEN311Form(forms.ModelForm):
    class Meta:
        model = SolicitudesOPEN311
        fields = ['titulo', 'categoria', 'direccion', 'descripcion', 'adjunto']

        def clean(self):
            clean_data = super().clean()
            titulo = clean_data.get('titulo')
            categoria = clean_data.get('categoria')
            direccion = clean_data.get('direccion')
            descripcion = clean_data.get('descripcion')
            adjunto = clean_data.get('adjunto')
           

            if not titulo or not categoria or not direccion or not descripcion or not adjunto:
                raise forms.ValidationError("Todos los campos deben ser completados.")
            
            return clean_data