from django import forms
from .models import Works



class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = '__all__'


class WorkTimeForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Pasirinkite norimus datos ir laiko formatą
    )

    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Pasirinkite norimus datos ir laiko formatą
    )

    class Meta:
        model = Works
        fields = ['darbas', 'start_time', 'end_time']


