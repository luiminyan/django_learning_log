from django.shortcuts import render

from logs.models import Topic


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
