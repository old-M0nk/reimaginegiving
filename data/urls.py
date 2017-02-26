from django.conf.urls import include, url
from data import views

urlpatterns = [
        url(r'^$', views.index, name='index')  #uncomment when the site needs to be put up

               ]