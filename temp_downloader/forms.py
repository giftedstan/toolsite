from django import forms
from .models import TemplateRecord

class TemplateDownloadForm(forms.ModelForm):
    class Meta:
        model=TemplateRecord
        fields=('temp',)
        widgets={
            'temp':forms.TextInput(attrs={'class':'form-control shadow-lg','placeholder':'Enter Template Name'})
        }