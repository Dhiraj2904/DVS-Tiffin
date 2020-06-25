#from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth import views as auth_views
from RCF.core import views
from RCF.core.views import PersonListView, showpastorder
from RCF.core.views import demo
from RCF.core import views as views2

urlpatterns = [
	path('', views.home, name='home'),
	path('user/', views.showpastorder, name='user'),
	#path('ordernowsubmission/', views.ordernowsubmission, name='ordernowsubmission'),
	path('myadmin/', views.adminlogin, name='loginpage'),
	path('menupage/', views.showmainmenu, name='menupage'),
	path('adminpage/', views.Insertrecord, name='adminpage'),
	path('',views.showmenu),
	path('signup/', views.register_view, name='signup'),
	path('login/', views.login_view, name='login'),
	#path('myadmin/', views.demo, name='demo'),
	path('myadmin/demo/', include('RCF.core.urls',namespace="reader_name")),
	path('myadmin/demo/', include('RCF.core.urls',namespace="reader_name2")),
	path('Delete/<int:id>',views.delrec),
	path('', views.showsociety),
	path('', PersonListView.as_view()),
	path('accounts/', include('django.contrib.auth.urls')),
   	path('admin/', admin.site.urls),
   	path('', views.showmainmenu),
   	#path('showorder/',views.showorder),
   #path('adminpage/templates/index.html/', views.save_alacarta, name='index'),
   path('',views.offtiffdisplay),
   path('adminpage/templates/index.html/',views.save_all, name='index'),
   path('', include('RCF.core.urls')),
  path('', views.insertalacarta),
  path('contact/',views.Contact, name='contact'),

]