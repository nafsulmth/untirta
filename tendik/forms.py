from dataclasses import fields
from django.forms import ModelForm
from django import forms
from tendik.models import Tendik

class FormTendik(ModelForm):
    class Meta: 
        model = Tendik 
        fields = '__all__'

        widgets = {
            'no' : forms.TextInput({'class':'form-control'}),
            'nip' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.FileInput({'class':'form-control'}),
        }