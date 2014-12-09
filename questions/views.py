from django.shortcuts import get_object_or_404, render

from questions.models import Question
from questions.forms import QuestionForm

import datetime

def index(request):
    latest_questions = Question.objects.order_by('-date')[:10]
    context = { 'latest_questions': latest_questions }
    return render(request, 'questions/index.html', context)

def show_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = { 'question': question }
    return render(request, 'questions/show.html', context)

def new_question(request):
    form = QuestionForm()
    context =  { 'form': form }
    return render(request, 'questions/new.html', context)


def create_question(request):
    form = QuestionForm(request.POST)
    new_question = form.save(commit=False)
    new_question.date = datetime.datetime.now()
    new_question.save()
    context = { 'question': new_question }
    return render(request, 'questions/show.html', context )
