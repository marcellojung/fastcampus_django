import re
from django import forms
from django.core.exceptions import ValidationError

def numCheck(value):
    if not 1 <= value <= 10:
        raise ValidationError('판매 수량은 1~10 사이만 가능합니다.')
        