from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]