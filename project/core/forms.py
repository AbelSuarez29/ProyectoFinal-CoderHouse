from django import forms

class BuscarNoticia(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField()
    fecha = forms.IntegerField()    
