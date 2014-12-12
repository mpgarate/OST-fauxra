from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404

from questions.models import Question, Answer, QuestionVote, AnswerVote
from questions.forms import QuestionForm, AnswerForm

import datetime

def index(request):
    latest_questions = Question.objects.order_by('-date')[:10]
    context = { 'latest_questions': latest_questions }
    return render(request, 'questions/index.html', context)

def show_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.order_by('votes').reverse()
    context = { 'question': question, 'answers': answers }
    return render(request, 'questions/show.html', context)

def new_question(request):
    if request.user.is_authenticated():
        form = QuestionForm()
        context =  { 'form': form }
        return render(request, 'questions/new.html', context)
    else:
        return redirect('accounts:sign_in')

def create_question(request):
    form = QuestionForm(request.POST)
    new_question = form.save(commit=False)
    new_question.date = datetime.datetime.now()
    new_question.user = request.user
    new_question.save()
    context = { 'question': new_question }
    return render(request, 'questions/show.html', context)

def new_answer(request, question_id):
    if request.user.is_authenticated():
        form = AnswerForm()
        context = { 'form': form , 'question_id': question_id }
        return render(request, 'questions/answers/new.html', context)
    else:
        return redirect('accounts:sign_in')

def create_answer(request, question_id):
    form = AnswerForm(request.POST)
    new_answer = form.save(commit=False)
    new_answer.date = datetime.datetime.now()
    question = get_object_or_404(Question, pk=question_id)
    new_answer.question = question
    new_answer.user = request.user
    new_answer.save()
    return redirect('questions:show', question_id)

def vote_up(request, question_id):
    return vote_foo_question(request, question_id, 1)

def vote_down(request, question_id):
    return vote_foo_question(request, question_id, -1)

def vote_foo_question(request, question_id, value):
    if not request.user.is_authenticated():
        return redirect('questions:show', question_id)

    user_id = request.user.id
    question = get_object_or_404(Question, pk=question_id)
    vote = QuestionVote.objects.filter(user_id=user_id, question=question).first()

    if vote is None:
        vote = QuestionVote()
        vote.user_id = user_id
        vote.question = question

    vote.value = value
    vote.save()
    question.update_votes()
    question.save()

    return redirect('questions:show', question_id)

def vote_up_answer(request, answer_id):
    return vote_foo_answer(request, answer_id, 1)
def vote_down_answer(request, answer_id):
    return vote_foo_answer(request, answer_id, -1)

def vote_foo_answer(request, answer_id, value):
    answer = get_object_or_404(Answer, pk=answer_id)
    question_id = answer.question_id

    if not request.user.is_authenticated():
        return redirect('questions:show', question_id)

    user_id = request.user.id
    vote = AnswerVote.objects.filter(user_id=user_id, answer=answer).first()

    if vote is None:
        vote = AnswerVote()
        vote.user_id = user_id
        vote.answer = answer

    vote.value = value
    vote.save()
    answer.update_votes()
    answer.save()

    return redirect('questions:show', question_id)
