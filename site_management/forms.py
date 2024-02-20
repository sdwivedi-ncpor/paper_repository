from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUsers
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUsers
        fields = '__all__'
        
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = UsernameField(label='Enter Username', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'password',
        }
))
    
class UserPassworChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserPassworChangeForm, self).__init__(*args, **kwargs)
    old_password = forms.CharField(
            label=_("Old password"),
            strip=False,
            widget=forms.PasswordInput(
                attrs={"autocomplete": "current-password", "autofocus": True,'class': 'form-control',
            'placeholder': '',
            'id': 'old_password',}
            ),
        )
    new_password1 = forms.CharField(
            label=_("New password"),
            strip=False,
            widget=forms.PasswordInput(
                attrs={'class': 'form-control',
            'placeholder': '',
            'id': 'new_password1',}
            ),
        )
    new_password2 = forms.CharField(
            label=_("Confirm password"),
            strip=False,
            widget=forms.PasswordInput(
                attrs={'class': 'form-control',
            'placeholder': '',
            'id': 'new_password2',}
            ),
        )