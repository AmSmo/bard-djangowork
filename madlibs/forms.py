from django import forms
from .models import Sonnet

class ChooseForm(forms.Form ):
    random = forms.RadioSelect(choices=['Random', 'Specific Sonnet'])
    sonnet = forms.IntegerField(max_value=154)
