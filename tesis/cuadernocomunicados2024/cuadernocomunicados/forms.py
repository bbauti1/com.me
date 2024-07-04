from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})
        super(CustomTextInput, self).__init__(*args, **kwargs)

class RegisterForm (UserCreationForm):
    username = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder' : "Ingrese usuario",
            'required' : True
        }
    ))
    email = forms.EmailField(widget=CustomTextInput(
        attrs={
            'placeholder' : "Ingrese email",
            'required' : True
        }
    ))

    dni = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder' : "Ingrese DNI",
            'required' : True
        }
    ))
    
    opciones = [
        ('preceptor', 'Preceptor'),
        ('profesor', 'Profesor'),
        ('responsable', 'Responsable'),
        ('alumno', 'Alumno'),
    ]

    tipo = forms.ChoiceField(choices=opciones , widget=forms.Select(
        attrs={
            'required' : True
        }
    ))

    nroCarnet = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder' : "Ingrese Numero de Carnet",
            'required' : True
        }
    ))

    first_name = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder' : "Ingrese nombre/s",
            'required' : True
        }
    ))
    last_name = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder' : "Ingrese apellido",
            'required' : True
        }
    ))
    password1 = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder' : "Ingrese contraseña",
            'required' : True
        }
    ))
    password2 = forms.CharField(widget=CustomTextInput(
        attrs={
            'placeholder' : "Repita contraseña",
            'required' : True
        }
    ))
    class Meta:
        model = User
        fields = ['username', 'email', 'dni', 'nroCarnet', 'first_name', 'last_name', 'password1', 'password2']