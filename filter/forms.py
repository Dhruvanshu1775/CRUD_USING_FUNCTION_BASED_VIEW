from django import forms
from .models import order


class orderform(forms.ModelForm):
    class Meta:
        model = order
        fields = '__all__'