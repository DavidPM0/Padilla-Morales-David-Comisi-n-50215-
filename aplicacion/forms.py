from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class BlogForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField(required=True)
    autor = forms.CharField(max_length=50, required=True)

class ProyectosForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(widget=forms.Textarea)
    fecha = forms.DateField(required=True)

class EventosForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    organizador = forms.CharField(max_length=100, required=True)
    fecha = forms.DateField(required=True)
    formato = forms.CharField(max_length=50, required=True)

class MerchandisingForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    valoraciones = forms.IntegerField(required=True)
    descripcion = forms.CharField(widget=forms.Textarea)
    precio = forms.FloatField(required=True)
    descuento = forms.FloatField(required=True)
    delivery = forms.CharField(max_length=50, required=True)

class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)