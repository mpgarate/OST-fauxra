from django.db import models

from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Question(models.Model):
    text = models.TextField()
    date = models.DateTimeField('date published')
    date_updated = models.DateTimeField('date updated', null=True)
    user = models.ForeignKey(User)
    votes = models.IntegerField(default=0)
    tags = TaggableManager()

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
    text = models.TextField()
    date = models.DateTimeField('date published')
    user = models.ForeignKey(User)
    votes = models.IntegerField(default=0)

    def update_votes(self):
        answer_votes = AnswerVote.objects.filter(answer=self)
        vote_count = 0

        for vote in answer_votes:
            vote_count += vote.value

        self.votes = vote_count

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
