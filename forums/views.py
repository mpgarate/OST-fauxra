from django.shortcuts import get_object_or_404, render

from forums.models import Question
import datetime

def index(request):
    latest_questions = Question.objects.order_by('-date')[:10]
    context = { 'latest_questions': latest_questions }
    return render(request, 'forums/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question': question }
    return render(request, 'forums/detail.html', context)

def new_question(request):
    return render(request, 'questions/new.html', {})


def create_question(request):
    form = QuestionForm(request.POST)
    new_question = form.save(commit=False)
    new_question.date = datetime.datetime.now()
    new_question.save()
