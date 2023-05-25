from django import forms
from General.models import *
from .models import *
from uuid import uuid4


class AddFacturaForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Cliente.objects.all(), label='Cliente', widget=forms.Select(attrs={'class':"form-select"}))
    rtn = forms.CharField(max_length=14, label='RTN', widget=forms.TextInput(attrs={'class':'form-control'}))


class UpdateFacturaForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Cliente.objects.all(), label='Cliente', widget=forms.Select(attrs={'class':"form-select"}))
    rtn = forms.CharField(max_length=14, label='RTN', widget=forms.TextInput(attrs={'class':'form-control'}))
    
class Meta:
    model = Factura
    fields = ['client']
    fields = ['rtn']