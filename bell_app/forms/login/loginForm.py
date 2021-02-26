from django import forms


class LoginForm(forms.Form):
    loginid = forms.CharField(label="ログインID")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())
