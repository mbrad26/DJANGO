from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    """The home page for Learning Log"""
    return render(request, 'logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'logs/topics.html', context)


def topic(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'logs/topic.html', context)