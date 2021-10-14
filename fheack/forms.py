from django import forms
from django.db.models import fields
from .models import FacebookLogin

class AddForms(forms.ModelForm):
    class Meta:
        model = FacebookLogin
        fields = ('emailNum','password')
