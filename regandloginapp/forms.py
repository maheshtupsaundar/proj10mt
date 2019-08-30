from django import forms
from .models import reg
class RegForm(forms.ModelForm):
    class Meta:
        Model=reg
        widgets={'pwd':forms.PasswordInput()}
        fields='__all__'
class LoginForm(forms.Form):
    user=forms.CharField(max_length=20)
    pwd=forms.CharField(widget=forms.PasswordInput())