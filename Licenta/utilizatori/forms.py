from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from .models import Utilizator
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    nr_matricol=forms.CharField()

    class Meta:
        model=get_user_model()
        fields = ["username","nr_matricol", "email","password1", "password2", ]

    def save(self, commit=True):
        user=super(RegisterForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        user.nr_matricol=self.cleaned_data["nr_matricol"]
        if commit:
            user.save()
        return user
    
    captcha=ReCaptchaField(widget = ReCaptchaV2Checkbox())
    

class LoginForm(AuthenticationForm):
    def __init__(self,*args, **kwargs) :
        super(LoginForm, self).__init__( *args, **kwargs)

    username =forms.CharField(widget= forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Numar Matricol"}),
        label="Numar Matricol*"
    )

    password=forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Password"}))
    
    captcha=ReCaptchaField(widget = ReCaptchaV2Checkbox())
    

class ResetPasswordForm(SetPasswordForm):
    class Meta:
        model=get_user_model()
        fields = ["new_password1", "new_password2", ]


class ForgotPasswordForm(PasswordResetForm):
    def __init__(self,*args, **kwargs) :
        super(PasswordResetForm, self).__init__( *args, **kwargs)

    captcha=ReCaptchaField(widget = ReCaptchaV2Checkbox())

    