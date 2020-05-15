from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.views.decorators.http import require_GET

from .models import Answer, Question


def test(request, *args, **kwargs):
    # answer = Answer.objects
    # print(type(answer))
    # answer = answer.filter(text__contains="a")
    # print(type(answer))
    # answer = answer.exclude(question_id=1)
    # print(type(answer))
    # answer = answer.order_by('text')
    # print(type(answer))
    # answer = answer.reverse()
    # print(type(answer))
    # answer = answer[0:2]
    # print(type(answer))
    # print(answer.count())
    # print(type(answer.count()))
    return HttpResponse('OK')


def show_page(request):
    try:
        page_num = int(request.GET.get('page'))
    except ValueError:
        page_num = 1
    except TypeError:
        page_num = 1
    limit = 10
    question = Question.objects.new()
    paginator = Paginator(question, limit)
    paginator.base_url = '/?page='
    page = paginator.page(page_num)

    return render(request, 'qa/question_paginator.html',
                  {'title': page_num, 'paginator': paginator, 'questions': page.object_list, 'page': page})


def show_popular(request):
    try:
        page_num = int(request.GET.get('page'))
    except ValueError:
        raise Http404()
    except TypeError:
        raise Http404()
    limit = 10
    question = Question.objects.popular()
    paginator = Paginator(question, limit)
    paginator.base_url = '/popular/?page='
    page = paginator.page(page_num)
    return render(request, 'qa/question_paginator.html',
                  {'title': page_num, 'paginator': paginator, 'questions': page.object_list, 'page': page})


def show_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'qa/question.html', {'title': question.title, 'text': question.text})
