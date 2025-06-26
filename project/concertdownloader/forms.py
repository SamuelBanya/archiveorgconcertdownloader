from django import forms
from .models import Band

class BandForm(forms.Form):
    band = forms.ModelChoiceField(queryset=Band.objects.all(), label="Band:")