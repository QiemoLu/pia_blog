from django import forms
from django.contrib.auth import authenticate, login
from myblog.models  import Category

class LoginForm(forms.Form):
    name = forms.CharField(
        label='Your name',
        max_length=20,
        error_messages={'required': 'Please enter your name'},
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(
        label='Your password',
        error_messages={'required': 'Please enter your password'},
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    #remember = forms.BooleanField(label='Remember')


class PostForm(forms.Form):

    title = forms.CharField(
        max_length=100,
        error_messages={'required': 'Please enter title'},
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        error_messages={'required': 'Please enter category'},
        widget=forms.Select(attrs={'class':
            'form-control'},choices=()))

    context = forms.CharField(
        max_length=10000,
        error_messages={'required': 'Please enter context'},
        widget=forms.Textarea(attrs={'class': 'form-control'}))


class CategoryForm(forms.Form):

    name = forms.CharField(
        max_length=10,
        error_messages={'required': 'can\'t notbe null'},
        widget=forms.TextInput(attrs={'class': 'form-control'}))


class AboutMeForm(forms.Form):

    aboutme = forms.CharField(
        max_length=10000,
        error_messages={'required': 'can\'t notbe null'},
        widget=forms.Textarea(attrs={'class': 'form-control'}))
