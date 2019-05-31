from django import forms
from .models import Task as Task_db


class TaskForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data['title']
        return title

    def clean_check(self):
        check = self.cleaned_data['check']
        return check

    def clean_date_to_do(self):
        date = self.cleaned_data['date_to_do']
        return date

    class Meta:
        model = Task_db
        fields = '__all__'
