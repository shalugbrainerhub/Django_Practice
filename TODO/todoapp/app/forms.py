from django import forms
from .models import Task

# class AddTaskForm(forms.Form):
#     class Meta:
#         model=Task
#         fields=['title']
    




class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    completed=forms.BooleanField()


class UpdateTaskForm(forms.Form):
    title = forms.CharField(max_length=100)
    completed=forms.BooleanField()