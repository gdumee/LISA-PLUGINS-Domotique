from django.conf.urls import patterns, url
from lisa.plugins.Domotique.web import views

urlpatterns = patterns('',
    url(r'^$',views.index),
)
