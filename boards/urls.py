from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^followers$', views.followers, name='followers'),
    url(r'^follow$', views.follow, name='follow'),
    url(r'^unfollow$', views.unfollow, name='unfollow'),

    url(r'^update$', views.update, name='update'),
    url(r'^destroy$', views.destroy, name='destroy'),
    url(r'^$', views.show, name='show'),
]