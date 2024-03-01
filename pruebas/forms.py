from django import forms
from .models import ArgentinaState

class ArgentinaStateForm(forms.ModelForm):
    class Meta:
        model = ArgentinaState
        fields = ['states']