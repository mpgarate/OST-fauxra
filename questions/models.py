from django.db import models
from django.forms import ModelForm

class Question(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.text


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['text']

