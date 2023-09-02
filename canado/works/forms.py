from django import forms
from .models import Works



class WorksForm(forms.ModelForm):
    # auto_id = forms.ModelChoiceField(queryset=models.Car.objects.all(), empty_label="Pasirinkite automobilį")
    class Meta:
        model = Works
        fields = '__all__'


