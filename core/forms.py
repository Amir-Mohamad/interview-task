# app/forms.py

from django import forms
from .models import Titanic

class TitanicForm(forms.ModelForm):
    class Meta:
        model = Titanic
        fields = '__all__'
