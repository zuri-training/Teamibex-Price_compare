from django import forms
from . models import Comment


class CreateComments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text', 'name', 'product')

        widgets = {
            'comment_text': forms.Textarea(attrs={'class': 'form-control'}),
        }
