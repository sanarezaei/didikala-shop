from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.http import request

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={'placeholder': 'نام کاربری خود را وارد کنید', 
                   'class': 'input-ui pr-2'
                   }), label='نام کاربری'
        ) 
    
    password = forms.CharField(
        widget= forms.TextInput(
            attrs={'placeholder': 'رمز عبور خود را وارد کنید.',
                   'class': 'input-ui pr-2'
                   }), label='رمز عبور'
        )
    
    
class RegisterForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={'placeholder': 'نام کاربری خود را وارد کنید',
                   'class': "input-ui pr-2"
                   }), 
        label='نام کاربری', 
        validators=[
            validators.MaxLengthValidator(20, 'نباید بیشتر از 20 کاراکتر باشد'),
            validators.MinLengthValidator(
                4, 'نام کاربری  نباید کمتر از 4 کاراکتر باشد')
            ]
    )
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'placeholder': 'ایمیل خود را وارد کنید', 'class': "input-ui pr-2"
            }), label='ایمیل'
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'placeholder': 'رمز خود را وارد کنید', 'class': 'input-ui pr-2'
        }), label='رمز عبور'
    )
    re_password = forms.CharField(
        widget = forms.PasswordInput(attrs={
            'placeholder': 'رمز  خود را مجددا وارد کنید',
            'class': 'input-ui pr-2' 
        }), label='تکرار رمز عبور'
    )
    
    def clean_username(self):
        username = self.clean_data.get('username')
        is_exist_user_by_username = User.objects.filter(
            username=username).exists()
        if is_exist_user_by_username:
            raise forms.ValidationError('این نام کاربری وجود ندارد')
        return username
    
    def clean_email(self):
        email = self.clean_data.get('email')
        is_exist_user_by_email = User.objects.filter(
            email=email).exists()
        if is_exist_user_by_email:
            raise forms.ValidationError('این ایمیل استفاده شده است')
        return email
    
    def clean_re_password(self):
        password = self.clean_data.get('password')
        re_password = self.clean_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('رمز های عبور مغایرت دارند')
        return password
