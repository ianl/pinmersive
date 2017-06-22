from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>[\w\-]+)/update$', views.update, name='update'),
    url(r'^(?P<id>[\w\-]+)/destroy$', views.destroy, name='destroy'),
    url(r'^(?P<id>[\w\-]+)/save$', views.save, name='save'),
    url(r'^(?P<id>[\w\-]+)$', views.show, name='show'),
]