from django import forms
from .models import BlogComment

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
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