from django import forms
from .models import Category
from .models import Post
from .models import Comment
from django.contrib.auth.models import User
from painless.models.error_messages import Messages 
msg = Messages()


class CSVImportForm(forms.Form):
    csv_file = forms.FileField


    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'email', 'content')




