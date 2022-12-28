from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

from django import forms




class fileform(ModelForm):
    class Meta:
        model = filesend
        fields = ['Name','Files','Status','id',]

class registerform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','is_teamleader','is_manager','is_employer']
