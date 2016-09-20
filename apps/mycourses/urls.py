from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^deletecourse/(?P<courseid>\w*)$', views.deletecourse),
    url(r'^confirmdelete/(?P<courseid>\w*)$', views.confirmdelete)
    
]