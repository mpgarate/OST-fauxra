from django import forms
from django.forms import ModelForm
from questions.models import Question, Answer

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'tags']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
