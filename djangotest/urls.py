from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^home/', views.home, name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^polls/', include('polls.urls')),
                       url(r'^users/', include('smartmin.users.urls')),
                       url(r'^smartminmodels/', include('smartminmodels.urls'))
                       )
