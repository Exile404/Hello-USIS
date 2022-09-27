from django import forms
class User(forms.Form):
    email=forms.CharField(max_length=100)
    psd= forms.CharField(max_length=164)
    ayear=forms.CharField(max_length=6)
    asession=forms.CharField(max_length=10)
    course=forms.CharField(max_length=7)