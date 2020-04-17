from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
from django import forms
from django.db import models


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email',)
