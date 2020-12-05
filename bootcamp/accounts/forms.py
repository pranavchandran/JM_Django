from django.contrib.auth import get_user_model
from django import forms
# check for unique email and username
User = get_user_model()

non_allowed_usernames = ['hacker']

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )
    password2 = forms.CharField(
    label = 'Confirm Password',
    widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'user-confirm-password'
            }
        )
    )


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'user-password'
            }
        )
    )

    # def clean(self):
    #     data = super().clean()
    #     username = data.get('username')
    #     password = data.get('password')

        # username = self.cleaned_data.get('username')
        # password = self.cleaned_data.get('password')


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("From security side we do not allowed you")
        # if qs.exists():
            # raise forms.ValidationError("This is an Invalid Username please pick another ")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This is an Invalid Email please pick another ")
        return email


