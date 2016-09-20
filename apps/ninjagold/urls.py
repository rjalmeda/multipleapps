from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^findgold$', views.findgold),
    url(r'^reset$', views.reset)
]
