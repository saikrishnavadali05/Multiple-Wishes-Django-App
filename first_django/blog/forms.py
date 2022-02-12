from django import forms
from .models import customerHBD

class customerHBD(forms.ModelForm):
    class Meta:
        model = customerHBD
        fields = '__all__'
