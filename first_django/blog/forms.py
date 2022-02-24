from django.forms import ModelForm
from .models import CustomerHBD

class CustomerHBDForm(ModelForm):
    class Meta:
        model = CustomerHBD
        fields = ['name', 'message', 'email', 'date' , 'time']
