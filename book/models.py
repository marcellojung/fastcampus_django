from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models
from django.urls import reverse
from django import forms
from .validators import numCheck

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해주세요')

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
