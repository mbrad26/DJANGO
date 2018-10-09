from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import NewTopic, NewEntry

# Create your views here.


def index(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'logs/index.html', context)


def topic(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'logs/topic.html', context)


def new_topic(request):

    if request.method != 'POST':
        form = NewTopic()
    else:
        form = NewTopic(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logs:index'))

    context = {'form': form}
    return render(request, 'logs/new_topic.html', context)


def new_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = NewEntry()
    else:
        form = NewEntry(data=request.POST)
        if form.is_valid():
            entry_new = form.save(commit=False)
            entry_new.topic = topic
            entry_new.save()
            return HttpResponseRedirect(reverse('logs:topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'logs/new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = NewEntry(instance=entry)
    else:
        form = NewEntry(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'logs/edit_entry.html', context)