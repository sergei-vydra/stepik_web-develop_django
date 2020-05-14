from django.shortcuts import render
from django.views.decorators import http
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')

