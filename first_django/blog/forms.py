from django.forms import ModelForm
from .models import customerHBD

class customerHBD(ModelForm):
    class Meta:
        model = customerHBD
        fields = ['name', 'message', 'email', 'date']
