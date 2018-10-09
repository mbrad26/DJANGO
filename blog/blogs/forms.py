from django import forms
from .models import BlogPost


class NewBlog(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}


class EditBlog(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}


