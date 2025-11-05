from django import forms
from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'name': 'message',
                'id': 'message',
                'rows': '3',  # You can use '1' or any number as per your need
                'placeholder': 'Message'
            })
        }