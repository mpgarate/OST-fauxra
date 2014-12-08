from django.shortcuts import render

from forums.models import Question

def index(request):
    latest_questions = Question.objects.order_by('-date')[:10]
    context = { 'latest_questions': latest_questions }
    return render(request, 'forums/index.html', context)

def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = { 'question': question }
    return render(request, 'forums/detail.html', context)