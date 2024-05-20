from django.shortcuts import render, redirect

from logs.models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def topics(request):
    """ show all topics"""
    # read data from databank
    topics = Topic.objects.order_by('-date_added')
    context = {'topics': topics}
    # send the read-data to template
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    """"Show topic and all entries for a given topic"""
    topic = Topic.objects.get(id=topic_id)
    # newest -> oldest
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'topic.html', context)


def new_topic(request):
    if request.method != "POST":
        # no data delivered
        form = TopicForm()
    else:
        # read data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs:topics')

    context = {'form': form}
    return render(request, 'new_topic.html', context)


def new_entry(request, topic_id):
    # Add the entry under specific topic
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            # Do not directly save into database
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            # redirect to topics/id after submitted
            return redirect('logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form, 'topic_id': topic_id}
    return render(request, 'new_entry.html', context)


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)
