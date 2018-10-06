"""Defines URL patterns for logs."""

from django.urls import path
from . import views

app_name = 'logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]

