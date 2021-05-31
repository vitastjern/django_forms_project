from django import forms
from django.core import validators
from django.forms.fields import CharField

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])


class UserForm(forms.Form):
    username = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    re_email = forms.EmailField(label='Please reenter your email')
    botcatcher = forms.CharField(required=False, 
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])   


