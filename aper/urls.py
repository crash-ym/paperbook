from django.conf.urls import include, url
from django.contrib import admin
from aper import views

app_name='aper'

urlpatterns=[
    #这里添加映射
    url(r'^index/$',views.index),
]