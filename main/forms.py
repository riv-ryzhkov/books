from .models import Book
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'text', 'published', 'count']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора'
        }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
        }),
            'published': TextInput(attrs={
                'class': "col-xs-4",
                'id': 'ex1',
                'placeholder': 'Введите год издания'
        }),
            'count': NumberInput(attrs={
                'class': "col-xs-2",
                'id': 'ex2',
                'placeholder': 'Введите количество книг'
        })
        }