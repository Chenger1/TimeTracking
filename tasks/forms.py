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
            'spent_hours',
            'spent_minutes',
            'scheduled_hours',
            'scheduled_minutes',
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
            'spent_hours': forms.NumberInput(attrs={'class': 'time_check currently'}),
            'spent_minutes': forms.NumberInput(attrs={'class': 'time_check currently'}),
            'scheduled_hours': forms.NumberInput(attrs={'class': 'time_check'}),
            'scheduled_minutes': forms.NumberInput(attrs={'class': 'time_check'}),
            'description': forms.Textarea(attrs={'style': 'height:150px;'}),
        }

    def clean(self):
        spent_hours = self.cleaned_data['spent_hours']
        spent_minutes = self.cleaned_data['spent_minutes']
        scheduled_hours = self.cleaned_data['scheduled_hours']
        scheduled_minutes = self.cleaned_data['scheduled_minutes']
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
