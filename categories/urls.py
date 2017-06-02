from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='categories'),
    url(r'^(?P<name>\w+)$', views.show, name='category'),
]