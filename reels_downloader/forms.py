from django import forms
from .models import ReelsRecord

class ReelsDownloadForm(forms.ModelForm):
    class Meta:
        model=ReelsRecord
        fields=('link',)
        widgets={
            'link':forms.URLInput(attrs={'class':'form-control shadow-lg','placeholder':'paste your video link here'})
        }