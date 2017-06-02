from django.conf.urls import url
from . import views
from boards import views as boards_views

urlpatterns = [
    url(r'^(?P<board_name>[\w\-]+)$', boards_views.show, name='board'),
]