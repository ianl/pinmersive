from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<name>\w+)$', views.show, name='category'),
]