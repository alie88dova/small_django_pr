from django import forms
from .models import *

class AddProductForm(forms.ModelForm):
    class Meta:

        model = ProductInfo
        fields = ["title", "content", "price"]
        widgets = {
            'title': forms.TextInput(attrs={"class": "market-input-title"}),
            'content' : forms.TextInput(attrs={"class" : "market-input-content"}),
            'price' : forms.TextInput()
        }
