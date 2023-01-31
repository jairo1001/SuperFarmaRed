from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.forms import Form 
class CustomUserCreationForm(UserCreationForm):
    username=forms.CharField(label='Usuario',min_length=5,max_length=150,help_text='Campo requerido.Se permiten letras y números')
    password1=forms.CharField(label='Password',widget=forms.PasswordInput,help_text="Ingrese un password de al menos 8 caracteres")
    password2=forms.CharField(label='Confirme password',widget=forms.PasswordInput, help_text= 'Vuelva a ingresar el password')

    def username_clean(self):
        username=self.cleaned_data['username'].lower()
        new=User.objects.filter(username=username);
        if new.count():
            raise ValidationError("Ese usuario ya existe")
        return username

    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Los password no coinciden")
        return password2

    def save(self,commit=True):
        user=User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1'],
            self.cleaned_data['password1']
        )
        return user


