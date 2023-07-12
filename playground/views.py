import time

from django.shortcuts import render


def say_hello(request):
    time.sleep(2)
    return render(request, 'hello.html')


def render_vue(request):
    return render(request, 'vue.html')

