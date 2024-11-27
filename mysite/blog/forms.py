from django import forms
from django.contrib.auth.models import User
from taggit.models import Tag
from .models import Comment
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, 
                               widget=forms.Textarea)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    title = forms.CharField(required=False, label='Search by title')
    # author = forms.CharField(required=False, label='Search by author')
    # tags = forms.CharField(required=False, label='Search by tags (comma separated)')