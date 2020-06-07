from django import forms
from .models import UsageMaster
from .models import Usage 
from django.core.exceptions import ValidationError

# def validate_genre(value):   

class UsageMasterForm(forms.ModelForm):
    class Meta:
        model = UsageMaster
        fields = ('genre',)

class UsageForm(forms.ModelForm):
    class Meta:
        model = Usage
        fields = ('date', 'genre', 'description','amount',)



