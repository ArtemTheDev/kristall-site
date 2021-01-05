from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'img', 'status']

        widgets = {
            'title':TextInput(attrs={
                    'placeholder': 'Введите назавание новости',
                    'name': 'newsTitle',
                    'type': 'text',
            }),
            'task': Textarea(attrs={
                'placeholder': 'Введите текст новости',
                'name': 'newsContent',
            }),

        }