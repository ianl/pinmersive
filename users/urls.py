from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^boards$', views.boards, name='boards'),
    url(r'^pins$', views.pins, name='pins'),
    url(r'^following$', views.following, name='following'),
    url(r'^followers$', views.followers, name='followers'),
    
    url(r'^follow$', views.follow, name='follow'),
    url(r'^unfollow$', views.unfollow, name='unfollow'),
    url(r'^(?P<board_name>[\w\-]+)$', views.board, name='board'),

    url(r'^$', views.boards, name='user'),
]