from django.conf.urls import include, url
from data import views

urlpatterns = [
        url(r'^$', views.index, name='index'),  #uncomment when the site needs to be put up
        url(r'^projectPage/(?P<pk>\d+)/$', views.projectPage, name='projectPage'),
        url(r'^checkOut/(?P<pk>\d+)/$', views.checkOut, name='checkOut'),
        url(r'^teamPage/', views.teamPage, name='teamPage'),
        url(r'^userPage/', views.userPage, name='userPage'),
        url(r'^viewAllProjects/(?P<cause>\([A-Z])\w+//$', views.viewAllProjects, name='viewAllProjects'),
        url(r'^contactUsPage/', views.contactUsPage, name='contactUsPage'),
               ]