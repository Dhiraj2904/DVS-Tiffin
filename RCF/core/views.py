from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from .forms import RegisterForm
#from .models import RegistrationData
from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponse
from .forms import UsersLoginForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from RCF.core.forms import RegisterForm
from RCF.core.models import EmpInsert, EmpInsert2, carta, orderdisplay, OrderNow, menudisplay, otdisplay, ltdisplay, dtdisplay
from django.views.generic import ListView

def Insertrecord(request):
	if request.method=='POST':
		saverecord=OrderNow()
		saverecord.ordernow_id=request.POST.get('ordernow_id')
		saverecord.tiffin_type=request.POST.get('tiffin_type')
		saverecord.subtiffin_type=request.POST.get('subtiffin_type')
		saverecord.from_date=request.POST.get('from_date')
		saverecord.to_date=request.POST.get('to_date')
		saverecord.total_amount=request.POST.get('total_amount')
		saverecord.author=request.user
		saverecord.save()
		
		#messages.success(request, 'record inserted successfully!!..')
		return render(request, 'user.html')
	else:
		res1=carta.objects.all()

		return render(request, 'adminpage.html', {'carta':res1})


def showsociety(request):
	results=showsoc.objects.all()
	return render(request, "signup.html", {"results":results})

def showmenu(request):
	r1=carta.objects.all()
	return render(request, "adminpage.html", {"carta":r1})

def showpastorder(request):
	res=OrderNow.objects.filter(author_id=request.user)
	return render(request, "user.html", {'OrderNow':res})


def showpastorder1(request):
	res=OrderNow.objects.all()
	
	return render(request, "user.html", {'OrderNow':res})

def showmainmenu(request):
	result1=menudisplay.objects.all()
	result2=otdisplay.objects.all()
	result3=ltdisplay.objects.all()
	result4=dtdisplay.objects.all()
	return render(request, "menupage.html", {'menudisplay':result1, 'otdisplay':result2, 'ltdisplay':result3, 'dtdisplay':result4})
def offtiffdisplay(request):
	result1=otdisplay.objects.all()
	return render(request, "menupage.html", {'otdisplay':result1})

@login_required
def index(request):
    return render(request,'user.html')

def odnow(request):
	return render(request, 'ordernow.html')

def home(request):
	return render(request, 'home.html')


def signup(request):
	
	
	return render(request, 'registration/signup.html',context)





def register_view(request):
	form = RegisterForm(request.POST or None)
	#profile_form=UserProfileForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		#profile=profile_form.save(commit=False)
		#profile.user=user
		#profile.save()
		
		username=form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")	
		user.set_password(password)
		user.save()
		
		messages.success(request, 'Account Registered Successfully!!')
		form=RegisterForm()
		#profile_form=UserProfileForm()

	context = {"form":RegisterForm}
	return render(request, "registration/signup.html", {
		"title" : "Register",
		"form" : form,
	})
@login_required
def login_view(request):
	form = UsersLoginForm(request.POST or None)
	
	if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username = username, password = password)
			login(request, user)
			if request.user.is_superuser:
				return render(request, 'adminpage.html')
			else:
				return render(request, 'user.html', {
				"form" : form,
				"title" : "Login",
	})
@login_required
def user(request):
    return render(request, 'user.html')
def menupage(request):
    return render(request, 'menupage.html')
def adminpage(request):
    return render(request, 'adminpage.html')
def support(request):
    return render(request, 'support.html')
def index(request):
    return render(request, 'index.html')


def showorder(request):

	return render_to_response('user.html', {'obj': models.OrderNow.objects.all()})

class PersonListView(ListView):
    model = EmpInsert2
    template_name = 'user.html'

def demo(request):
	return render(request, 'demo.html')



