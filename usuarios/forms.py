from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    grupo = forms.ModelChoiceField(queryset=Group.objects.filter(name__in=["Cliente", "Usuário", "Vendedor"]), required=True)

    class Meta:
        model = User
        fields = ['username', 'grupo', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))

        return e

        
