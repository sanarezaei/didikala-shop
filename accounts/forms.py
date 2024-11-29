from django import forms

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