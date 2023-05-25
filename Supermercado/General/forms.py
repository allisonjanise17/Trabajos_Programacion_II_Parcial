from django import forms
from .models import *

class AddcargoForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre del Cargo', widget=forms.TextInput(attrs={'class':'form-control'}))



class UpdateCargoForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label='Nombre del Cargo', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Cargo
        fields = ['name']

class AddClienteForm(forms.Form):
    person =  forms.ModelChoiceField(queryset=Persona.objects.all(), label='Persona', widget=forms.Select(attrs={'class':'form-select'}))
    address = forms.CharField(max_length=255, label='Direccion', widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))


class UpdateClienteForm(forms.ModelForm):
    person =  forms.ModelChoiceField(queryset=Cliente.objects.all(), label='Persona', widget=forms.Select(attrs={'class':'form-select'}))
    address = forms.CharField(max_length=255, label='Address', widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Cargo
        fields = ['address']
        fields = ['phone']

class AddUsuarioForm(forms.ModelForm):
    person =  forms.ModelChoiceField(queryset=Usuario.objects.all(), label='Persona', widget=forms.Select(attrs={'class':'form-select'}))
    email = forms.CharField(max_length=100, label='Correo Electronico',widget=forms.TextInput(attrs={'class':'form-control'}) )
    address = forms.CharField(max_length=255, label='Direccion', widget=forms.TextInput(attrs={'class':'form-control'}))
    phone =forms.CharField(max_length=8, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))



    
