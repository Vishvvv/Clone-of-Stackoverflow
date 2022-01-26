from django import forms
from django.core import validators
from .models import Questions

# class Question(forms.Form):
#     question_text = forms.CharField(widget=forms.Textarea)
#     answer_text = forms.CharField(widget=forms.Textarea)

class Questionanswer(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['question','answer']
        help_text = {'question': 'Enter your Question here'}
        # widgets = {'question': 'forms.Textarea',
                    # 'answer': 'forms.Textarea'}