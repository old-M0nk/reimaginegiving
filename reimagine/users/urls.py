from django.conf.urls import include, url
from users import views

urlpatterns = [
        url(r'^$', views.index, name='index')
               ]