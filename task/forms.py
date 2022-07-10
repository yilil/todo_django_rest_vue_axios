from .models import Task
from django import forms


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'description'
        ]