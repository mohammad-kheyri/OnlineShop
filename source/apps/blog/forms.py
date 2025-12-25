from django import forms
from .models import BlogComment, Blog, BlogTag

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
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



class CreateBlogForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter tags (comma separated)'
        })
    )

    class Meta:
        model = Blog
        fields = ('title', 'body', 'category', 'image')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter blog title',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your blog content here...',
                'rows': 3,
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

