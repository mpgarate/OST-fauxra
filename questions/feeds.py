from django.shortcuts import get_object_or_404

from django.core.urlresolvers import reverse

from django.contrib.syndication.views import Feed

from django.template.defaultfilters import truncatechars

from questions.models import Question, Answer

class LatestAnswersFeed(Feed):
    link = "/"

    def get_object(self, request, question_id):
        return get_object_or_404(Question, pk=question_id)

    def items(self, question):
        return Answer.objects.filter(question=question).order_by('-date')[:10]

    def title(self, item):
        return "Latest answers on Fauxra for the question: %s" % item.text

    def item_title(self, item):
        return item.text

    def item_link(self, item):
        return reverse("questions:show", args=[item.question.id])


class LatestQuestionsFeed(Feed):
    title = "Latest questions from Fauxra"
    link = "/"
    description = "See the latest questions posted to Fauxra."

    def items(self):
        return Question.objects.order_by('-date')[:10]

    def item_title(self, item):
        return truncatechars(item.text, 500)

    def item_link(self, item):
        return reverse("questions:show", args=[item.id])

