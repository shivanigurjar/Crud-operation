from django.core import validators
from django import forms
from .models import your_model

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = your_model
        fields= ['First_name','Last_name','Password']
        widgets = {
            'First_name' : forms.TextInput(attrs={'class':'form-control'}),
            'Last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'Password' : forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }
