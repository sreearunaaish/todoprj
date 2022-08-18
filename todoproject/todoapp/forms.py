from django import forms
from .models import task


class task_form(forms.ModelForm):
    class Meta:
        model=task
        fields=('name','priority','date')