from django import forms
from .models import Works



class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = '__all__'


class WorkTimeForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['darbas', 'start_time', 'end_time']


