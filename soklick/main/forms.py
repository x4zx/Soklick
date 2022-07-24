from django import forms
from main.models import LinksUsers

class LinksUser(forms.ModelForm):
    class Meta:
        model = LinksUsers
        fields = ['user', 'before_url', 'after_url']
        widgets = {'user': forms.HiddenInput()}