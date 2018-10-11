from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import NewTopic, NewEntry
from .models import Topic, Entry

# Create your views here.


def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404


def index(request):

    return render(request, 'logs/index.html')


@login_required
def topics(request):

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'logs/topics.html', context)


@login_required
def topic(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'logs/topic.html', context)


@login_required
def new_topic(request):

    if request.method != 'POST':
        form = NewTopic()
    else:
        form = NewTopic(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('logs:topics'))
    context = {'form': form}
    return render(request, 'logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        form = NewEntry()
    else:
        form = NewEntry(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('logs:topic', args=[topic.id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)
    if request.method != 'POST':
        form = NewEntry(instance=entry)
    else:
        form = NewEntry(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logs:topic', args=[topic.id]))
    context = {'form': form, 'topic': topic, 'entry': entry}
    return render(request, 'logs/edit_entry.html', context)



