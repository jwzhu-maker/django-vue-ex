from django.shortcuts import render


def render_index(request):
    return render(request, 'vue_vite.html')


def render_vue(request):
    return render(request, 'vue.html')
