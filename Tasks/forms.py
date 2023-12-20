
from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'submission_date', 'priority']
        widgets = {
            'submission_date': forms.DateInput(attrs={'type': 'date'})
        }


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'submission_date', 'priority']
        widgets = {
            'submission_date': forms.DateInput(attrs={'type': 'date'})
        }
