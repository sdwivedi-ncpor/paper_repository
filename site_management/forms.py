from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUsers


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUsers
        fields = '__all__'