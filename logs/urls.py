from django.urls import path
from . import views

app_name = 'logs'


urlpatterns = [
    # starting page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    # add new entry under a topic: take topic_id as an argument
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]