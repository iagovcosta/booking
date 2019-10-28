from django import forms
from .models import Login

class Login(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['nome', 'senha']