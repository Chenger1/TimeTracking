from django import forms
from django.core.exceptions import ValidationError

from .models import Task
from .models import Category


class TaskForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, user, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user_id=user.id)

    class Meta:
        model = Task
        fields = [
            'name',
            'time_spent_hour',
            'time_spent_minute',
            'time_scheduled_hour',
            'time_scheduled_minute',
            'description',
            'category',
            'time_trigger'
        ]
        labels = {
            'time_trigger': 'Scheduled this action'
        }
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name_input'}),
            'slug': forms.TextInput(attrs={}),
            'time_trigger': forms.CheckboxInput(attrs={'type': 'checkbox'}),
            'time_spent_hour': forms.NumberInput(attrs={'class': 'time_check currently'}),
            'time_spent_minute': forms.NumberInput(attrs={'class': 'time_check currently'}),
            'time_scheduled_hour': forms.NumberInput(attrs={'class': 'time_check'}),
            'time_scheduled_minute': forms.NumberInput(attrs={'class': 'time_check'}),
            'description': forms.Textarea(attrs={'style': 'height:150px;'}),
        }

    def clean(self):
        time_spent_hour = self.cleaned_data['time_spent_hour']
        time_spent_minute = self.cleaned_data['time_spent_minute']
        time_scheduled_hour = self.cleaned_data['time_scheduled_hour']
        time_scheduled_minute = self.cleaned_data['time_scheduled_minute']
        time_trigger = self.cleaned_data['time_trigger']


class CategoryForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.user_id = user.id

    class Meta:
        model = Category
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        name = self.cleaned_data['name']
        user_category = Category.objects.filter(user_id=self.user_id)
        if user_category:
            for item in user_category:
                if name == item.name:
                    raise ValidationError({'name': 'This category already register.'},
                                          code='name exists')
