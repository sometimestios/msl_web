from django import forms
from .models import Target,Log,Task


class TargetForm(forms.ModelForm):
    class Meta:
        model = Target
        fields = ['name', 'ip', 'os', 'service', 'desc']