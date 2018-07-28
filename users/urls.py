from django.conf.urls import url, include
from . import views

import boards.views as boards_views
import pins.views as pins_views

urlpatterns = [
    url(r'^boards/create$', boards_views.create, name='boards_create'),
    url(r'^boards$', views.boards, name='boards'),

    url(r'^pins/create$', pins_views.create, name='pins_create'),
    url(r'^pins$', views.pins, name='pins'),

    url(r'^following$', views.following, name='following'),
    url(r'^followers$', views.followers, name='followers'),
    url(r'^follow$', views.follow, name='follow'),
    url(r'^unfollow$', views.unfollow, name='unfollow'),

    url(r'^(?P<board_name>[\w\- ]+)/', include('boards.urls', namespace='boards')),

    url(r'^$', views.boards, name='user'),
]