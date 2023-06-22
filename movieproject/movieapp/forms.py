from django import forms

from .models import display


class Movieform(forms.ModelForm):
    class Meta:
        model=display
        fields=['name','desc','year','img']
