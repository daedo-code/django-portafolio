from django import forms
from .models import Mensaje
from django.contrib.auth.forms import AuthenticationForm

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'telefono', 'cuerpo']  # solo los que completa el cliente
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
            # 'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje aquí...', 'rows': 5}),
        }
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            # 'asunto': 'Asunto',
            'cuerpo': 'Mensaje',
        }

class LoginForm(AuthenticationForm):
  username = forms.CharField(
      widget=forms.TextInput(attrs={
          "class": "form-control",  # Bootstrap
          "placeholder": "Usuario",
      })
  )
  password = forms.CharField(
      widget=forms.PasswordInput(attrs={
          "class": "form-control",
          "placeholder": "Contraseña",
      })
  )
