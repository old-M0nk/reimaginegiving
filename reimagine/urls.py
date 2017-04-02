"""reimagine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from core import views as core_views
from data import views
from users.views import login_view, logout_view, register_view, userPage, NGOformPage
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'trust.views.home', name='home'),
    # url(r'^trust/', include('trust.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

        url(r'^$', views.index, name='index'),  #uncomment when the site needs to be put up
        url(r'^projectPage/(?P<pk>\d+)/$', views.projectPage, name='projectPage'),
        url(r'^checkOut/(?P<pk>\d+)/$', views.checkOut, name='checkOut'),
        url(r'^teamPage/', views.teamPage, name='teamPage'),
        url(r'^userPage/', userPage, name='userPage'),
        url(r'^viewAllProjects/(?P<cause>\w+)/(?P<funding>\w+)/$', views.viewAllProjects, name='viewAllProjects'),
        url(r'^contactUsPage/', views.contactUsPage, name='contactUsPage'),

        url(r'^home/$', core_views.home, name='home'),
        url(r'^login/$', login_view, name='login'),
        url(r'^register/$', register_view, name='register'),
        # url(r'^logout/$', auth_views.logout, name='logout'),
        url(r'^logout/$', logout_view, name='logout'),
        url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

        url(r'^admin/', include(admin.site.urls)),
        url(r'^comingsoon', include('users.urls')),
        url(r'^develop/$', NGOformPage, name='NGOform'),
        url(r'^payment_redirect/',views.payment_redirect, name='payment_redirect'),

        url(r'^aboutus/', views.aboutus, name='aboutus'),
        url(r'^terms/', views.terms, name='terms'),
        url(r'^refund/', views.refund, name='refund'),
        url(r'^privacy/', views.privacy, name='privacy'),
        url(r'^pricing/', views.pricing, name='pricing'),
        url(r'^Success/',views.success),
        url(r'^Failure/',views.failure),
    # url(r'^$', include('data.urls')), # for the coming soon page   #comment out when the site needs to be put up
    # url(r'^main/', include('data.urls')), # for the main pages   #uncomment when the site needs to be put up
    # url(r'^users/', include('users.urls')),# once the user logs in...
    # url(r'^staff/', include('staff.urls')), # for the staff portal

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
