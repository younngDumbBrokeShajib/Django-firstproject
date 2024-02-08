from django import forms
from .models import Contact

class contactForm(forms.Form):
    
    name=forms.CharField(max_length=100, required=True,label="Your name")
    phone=forms.CharField(max_length=100,required=True,label="Your phone")
    content=forms.CharField(max_length=1000,required=True,label="Content")
    