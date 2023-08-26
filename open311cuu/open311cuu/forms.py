from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
#Agrega el campo para email
    email = forms.EmailField()
    
    class Meta:
        #Especifica el modelo con el que se relaciona el formulario
        model = User
        #Especifíca los campos que se mostrarán en el formulario y su orden
        fields = ['username', 'email', 'password1', 'password2']
