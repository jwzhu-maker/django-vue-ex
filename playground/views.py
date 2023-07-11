from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return render(request, 'hello.html')


def render_vue(request):
    return render(request, 'vue.html')

