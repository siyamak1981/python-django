# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length = 30, label = 'نام کاربری')
#     # first_name = forms.CharField(max_length = 30, label = 'نام', required = True, help_text = 'Enter ur firsname.')
#     # last_name = forms.CharField(max_length = 30, label='نام خانوادگی', required = True, help_text = 'Enter ur lastname.')
#     # email = forms.EmailField(label='ایمیل')
#     password1 = forms.CharField(label = 'رمز عبور', widget = forms.PasswordInput)
#     password2 = forms.CharField(label = 'تکرار رمز عبور', widget = forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
        


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignInForm(AuthenticationForm):
    username = forms.EmailField(label = 'ایمیل', required = True)
    password = forms.CharField(label = 'رمز عبور',widget = forms.PasswordInput)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = 'ایمیل', max_length=30, required = True)
    first_name = forms.CharField(label = 'نام', max_length=30, required = True, help_text = 'enter your first name.')
    last_name = forms.CharField(label = 'نام خانوادگی', max_length=30, required = True)
    password1 = forms.CharField(label = 'رمز عبور', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'تکرار رمز عبور', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2') 