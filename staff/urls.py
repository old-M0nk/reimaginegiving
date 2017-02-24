from django.conf.urls import include, url
from staff import views

urlpatterns = [
        url(r'^$', views.index, name='page')
               ]