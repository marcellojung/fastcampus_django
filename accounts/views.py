from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.conf import settings
from django.urls import reverse_lazy
from .forms import SignupForm


def signup(request):
    pass

def profile(request):
    return render(request, 'accounts/profile.html')

class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')
    template_name = 'accounts/password_change_form.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)

class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'accounts/password_reset_form.html'
    def form_valid(self, form):
        messages.info(self.request, '암호 변경 메일을 발송하였습니다.')
        return super().form_valid(form)

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('login')
    template_name = 'accounts/password_reset_confirm.html'
    def form_valid(self, form):
        messages.info(self.request, '암호 리셋을 완료했습니다.')
        return super().form_valid(form)

    