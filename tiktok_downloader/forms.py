from django import forms
from .models import TiktokRecord

class TiktokDownloadForm(forms.ModelForm):
    class Meta:
        model=TiktokRecord
        fields=('link',)
        widgets={
            'link':forms.URLInput(attrs={'class':'form-control shadow-lg','placeholder':'paste your video link here'})
        }