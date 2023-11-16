#Importamos forms
from django import forms

#creamos la calse ContactForm que hereda de la clase padre Forms
#Demeos indicar los campos y su tipo


class FormPrestamo(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    dni = forms.CharField(label="DNI", required=True)
    tipo = forms.ChoiceField(widget=forms.Select, choices = [("1","HIPOTECARIO"),("2","PERSONAL"),("3","PRENDARIO")])
    fecha = forms.DateField(label="Fecha", required=True)
    monto = forms.IntegerField(label="Monto", required=True)