from django import forms
from .models import *

class AddPostForm(forms.Form):
    content = forms.CharField(widget=forms.TextInput(), label="")