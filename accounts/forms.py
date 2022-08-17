from django import forms
from django.core.validators import validate_email
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import Profile

class SignupForm(UserCreationForm):
    pass

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].validators = [validate_email]

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = user.username
    #     if commit:
    #         user.save()
    #     return user

class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='손흥민의 등번호는?')
    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 7:
            raise forms.ValidationError('Wrong Answer!')
        return answer
