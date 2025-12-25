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
                'rows': '3', 
                'placeholder': 'Message'
            })
        }