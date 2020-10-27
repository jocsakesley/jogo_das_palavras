from django import forms
from .models import SubmitModel

class SubmitForm(forms.Form):
    letter = forms.CharField(max_length=1)
