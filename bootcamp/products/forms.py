from django import forms
from .models import Product

# class ProductForm(forms.Form):
#     title = forms.CharField()

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "image"
        ]
    
    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data)<4:
            raise forms.ValidationError('minimum chars is 4')
        return data

    def clean_content(self):
        data = self.cleaned_data.get('content')
        if len(data)<4:
            raise forms.ValidationError('minimum chars is 4')
        return data

