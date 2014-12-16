from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from questions.models import Question, Answer, QuestionVote, AnswerVote
from questions.forms import QuestionForm, AnswerForm
from django.db.models import Count

from taggit.models import Tag

import datetime

def index(request):
    questions_list = Question.objects.annotate(
        null_last_activity_date=Count('last_activity_date')
    ).order_by('-null_last_activity_date', '-last_activity_date')
    paginator = Paginator(questions_list, 10)

    page = request.GET.get('page')

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    context = { 'questions': questions }
    return render(request, 'questions/index.html', context)

def tagged(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    questions_list = Question.objects.filter(tags=tag)

    paginator = Paginator(questions_list, 10)

    page = request.GET.get('page')

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    context = { 'questions': questions, 'tag': tag }
    return render(request, 'questions/tagged.html', context)

def show_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.order_by('votes').reverse()
    context = { 'question': question, 'answers': answers }
    question.tags
    return render(request, 'questions/show.html', context)

def new_question(request):
    if request.user.is_authenticated():
        form = QuestionForm()
        context =  { 'form': form }
        return render(request, 'questions/new.html', context)
    else:
        return redirect('accounts:sign_in')

def create_question(request):
    if request.user.is_authenticated():
        form = QuestionForm(request.POST)

        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.date = datetime.datetime.now()
            new_question.user = request.user
            new_question.save()

            tags = form.cleaned_data['tags']
            new_question.tags.clear()
            for tag in tags:
                new_question.tags.add(tag)

            new_question.save()
            return redirect('questions:show', question_id = new_question.id)
        else:
            return redirect('questions:new')
    else:
        return redirect('/')

def update_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if not request.user == question.user:
        return redirect('questions:show', question)

    form = QuestionForm(request.POST)

    if form.is_valid():
        tags = form.cleaned_data['tags']
        question.tags.clear()
        for tag in tags:
            question.tags.add(tag)

        question.date_updated = datetime.datetime.now()
        question.text = form.cleaned_data['text']
        question.save()

        return redirect('questions:show', question_id=question_id)
    else:
        return redirect('questions:edit', question_id=question_id)

def update_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if not request.user == answer.user:
        return redirect('questions:show', answer.question)

    form = AnswerForm(request.POST)

    if form.is_valid():
        answer.date_updated = datetime.datetime.now()
        answer.text = form.cleaned_data['text']
        answer.save()

        return redirect('questions:show', answer.question.id)

    context = { 'form': form }
    return render(request, 'questions:edit_answer', context)

def edit_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if not request.user == question.user:
        return redirect('questions:show', question)

    form = QuestionForm(instance=question)
    context = { 'form': form, 'question': question }
    return render(request, 'questions/edit.html', context)

def edit_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if not request.user == answer.user:
        return redirect('questions:show', answer.question)

    form = AnswerForm(instance=answer)
    context = { 'form': form, 'question': answer.question, 'answer': answer }
    return render(request, 'answers/edit.html', context)

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
