from django.contrib import admin
from django.urls import path, include

from RCF.core import views
app_name = "reader"
urlpatterns = [
	path('user/', views.showmainmenu, name='user'),
	path('', views.readexcel,name='readexcel'),
	path('', views.showpastorder, name='demo'),
	path('', views.readexcel2, name='readexcel2'),
]