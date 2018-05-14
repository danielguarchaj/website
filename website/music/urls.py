from django.conf.urls import url
from . import views

urlpatterns = [
    #   music/
    url(r'^$', views.index, name='index'), # if the url is empty is being kinda like the index for each app

    #   music/712 (album's id)
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
