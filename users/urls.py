from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^boards$', views.boards, name='boards'),
    url(r'^pins$', views.pins, name='pins'),

    url(r'^(?P<board_name>[\w\-]+)$', views.board, name='board'),

    url(r'^$', views.boards, name='user'),
]