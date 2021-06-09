from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    institution_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'institution'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password'}))