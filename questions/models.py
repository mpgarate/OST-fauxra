from django.db import models

from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from django.contrib.syndication.views import Feed

from django.template.defaultfilters import truncatechars

class Question(models.Model):
    text = models.TextField()
    date = models.DateTimeField('date published')
    date_updated = models.DateTimeField('date updated', null=True)
    user = models.ForeignKey(User)
    votes = models.IntegerField(default=0)
    tags = TaggableManager(blank=True)

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
        text = self.text

        # wrap image urls with img tag
        # text = re.sub(r'(http[s]{0,1}://[\w]*\.[\w\/\.]*[^\s"\'"])',
         #             r'<img src="\1" />', text)

        # wrap non-image urls with anchor tag
        # text = re.sub(r'(http[s]{0,1}://[\w]*\.[\w\/\.]*[^\s]([\s]|$)((?!\.jpg)))',
         #      r'<a href="\1">\1</a>', text)

        return text

class QuestionVote(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    value = models.IntegerField()

class AnswerVote(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
    value = models.IntegerField()


class LatestQuestionsFeed(Feed):
    title = "Latest questions from Fauxra"
    link = "/"
    description = "See the latest questions posted to fauxra."

    def items(self):
        return Question.objects.order_by('-date')[:10]

    def item_title(self, item):
        return truncatechars(item.text, 500)

    def item_link(self, item):
        return reverse("questions:show", args=[item.id])

