from django import forms
from django.core.exceptions import ValidationError
from .models import Book

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')

class BookForm(forms.Form):
    title = forms.CharField(label='제목')
    author = forms.CharField(label='저자', validators=[min_length_3_validator])
    publisher = forms.CharField(label='출판사', required=False)

    def save(self, commit=True):
        book = Book(**self.cleaned_data)
        if commit:
            book.save()
        return book
        