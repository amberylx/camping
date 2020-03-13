from django import forms


class LoginForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
