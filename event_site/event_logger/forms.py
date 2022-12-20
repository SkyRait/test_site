from .models import Event
from django.forms import ModelForm, TextInput, Textarea


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),

            'point': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Point'
            }),

            'place': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Place'
            }),

            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            })
        }


