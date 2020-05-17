from django.contrib import admin
from django.urls import path, include

from RCF.core import views

urlpatterns = [
	path('user/', views.showmainmenu, name='user'),
		
]