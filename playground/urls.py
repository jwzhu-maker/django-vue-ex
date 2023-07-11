from django.urls import path
from .import views

urlpatterns = [
    path('', views.say_hello, name='say_hello'),
    path('vue/', views.render_vue, name='render_vue'),
]
