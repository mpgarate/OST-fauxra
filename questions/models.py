from django.db import models

from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')
    user = models.ForeignKey(User)
    votes = models.IntegerField()

    def update_votes(self):
        question_votes = QuestionVote.objects.filter(question=self)
        vote_count = 0

        for vote in question_votes:
            vote_count += vote.value

        self.votes = vote_count

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.text

class QuestionVote(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    value = models.IntegerField()

class AnswerVote(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
    value = models.IntegerField()
