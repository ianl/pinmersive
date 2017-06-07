from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^boards$', views.boards, name='boards'),
    url(r'^pins$', views.pins, name='pins'),
    url(r'^$', views.boards, name='user'),

    url(r'^following$', views.following, name='following'),
    url(r'^followers$', views.followers, name='followers'),
    url(r'^follow$', views.follow, name='follow'),
    url(r'^unfollow$', views.unfollow, name='unfollow'),

    url(r'^(?P<board_name>[\w\-]+)/', include('boards.urls', namespace='boards')),
]