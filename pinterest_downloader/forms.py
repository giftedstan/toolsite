from django import forms
from .models import PinterestRecord

class PinterestDownloadForm(forms.ModelForm):
    class Meta:
        model=PinterestRecord
        fields=('link',)
        widgets={
            'link':forms.URLInput(attrs={'class':'form-control shadow-lg','placeholder':'paste your video link here'})
        }