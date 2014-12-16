from django.db import models

from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from django.contrib.syndication.views import Feed

import datetime

class Question(models.Model):
    text = models.TextField()
    date = models.DateTimeField('date published')
    date_updated = models.DateTimeField('date updated', null=True)
    user = models.ForeignKey(User)
    votes = models.IntegerField(default=0)
    tags = TaggableManager(blank=True)
    last_activity_date = models.DateTimeField('last activity date', null=True)

    def save(self, *args, **kwargs):
        self.last_activity_date = datetime.datetime.now()
        super(Question, self).save(*args, **kwargs)

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
    date_updated = models.DateTimeField('date updated', null=True)
    user = models.ForeignKey(User)
    votes = models.IntegerField(default=0)

    def update_votes(self):
        answer_votes = AnswerVote.objects.filter(answer=self)
        vote_count = 0

        for vote in answer_votes:
            vote_count += vote.value

        self.votes = vote_count

    def save(self, *args, **kwargs):
        self.question.last_activity_date = datetime.datetime.now()
        self.question.save()
        super(Answer, self).save(*args, **kwargs)

    def __str__(self):
        text = self.text

        return text

class QuestionVote(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    value = models.IntegerField()

class AnswerVote(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
    value = models.IntegerField()

class LatestAnswersFeed(Feed):
    link = "/"

    def get_object(self, request, question_id):
        return get_object_or_404(Question, pk=question_id)

    def items(self, question):
        return Answer.objects.filter(question=question).order_by('-date')

    def title(self, item):
        return "Latest answers on Fauxra for the question: %s" % item.question.text

    def item_title(self, item):
        return item.text

    def item_link(self, item):
        return reverse("questions:show", args=[item.question.id])


class LatestQuestionsFeed(Feed):
    title = "Latest questions from Fauxra"
    link = "/"
    description = "See the latest questions posted to Fauxra."

    def items(self):
        return Question.objects.order_by('-date')

    def item_title(self, item):
        return truncatechars(item.text, 500)

    def item_link(self, item):
        return reverse("questions:show", args=[item.id])