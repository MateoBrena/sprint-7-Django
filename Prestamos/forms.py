#Importamos forms
from django import forms

class FormPrestamo(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control'}))
    apellido = forms.CharField(label="Apellido", required=True,widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control'}))
    dni = forms.CharField(label="DNI", required=True,widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control'}))
    tipo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices = [("HIPOTECARIO","HIPOTECARIO"),("PERSONAL","PERSONAL"),("PRENDARIO","PRENDARIO")])
    fecha = forms.DateField(label="Fecha Inicio", required=True, widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd','class': 'form-control'}))
    monto = forms.IntegerField(label="Monto", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))