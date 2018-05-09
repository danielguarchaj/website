from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # if the url is empty is being kinda like the index for each app
]
