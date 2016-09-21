from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/(?P<courseid>\w*)', views.register),
    url(r'^reset$', views.reset)
]
