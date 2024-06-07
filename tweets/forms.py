from .models import Tweet
from django import forms

class TweetForm(forms.ModelForm):
    class Meta:
      model = Tweet
      fields = ['image', 'text']
      widgets = {
         'text': forms.Textarea(attrs={'placeholder': 'Text', 'rows': 10}),
      }
      labels = {
         'text': 'テキスト',
      }