from django.urls import path,re_path

from . import views

urlpatterns = [
    #main page
    path('', views.index, name='index'),
    re_path('^topics/$',views.topics, name='topics'),
    #one specified topic detail page
    re_path('^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    re_path('^new_topic/$', views.new_topic, name='new_topic'),
    re_path('^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    re_path('^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]