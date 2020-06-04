from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from .forms import RegisterForm
#from .models import RegistrationData
from django.contrib import messages

from django.http import HttpResponseRedirect, HttpResponse
from .forms import UsersLoginForm, AdminLoginForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from RCF.core.forms import RegisterForm, ContactForm
from RCF.core.models import EmpInsert, EmpInsert2, carta, carorder, orderdisplay, OrderNow, menudisplay, otdisplay, ltdisplay, dtdisplay, alacartaorder
from django.views.generic import ListView
from django.template import RequestContext
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMessage
import openpyxl


def save_all(request):
	if request.method=='POST':
	
		post=carorder()
		post.carid= request.POST.get('carid')
		post.carmenu= request.POST.get('carmenu')
		post.carqty= request.POST.get('carqty')
		post.caramt=request.POST.get('caramt')
		post.author=request.user
		post.save()
		messages.success(request, "Record Saved Successfully!!")
		return render(request, 'index.html')  

	else:
		res1=alacartaorder.objects.all()
		return render(request, 'index.html', {'alacartaorder':res1})

	return render(request,'adminpage.html')





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


@login_required
def insertalacarta(request):
	if request.method=='POST':
		saverecord=alacartaorder()
		saverecord.aid=request.POST.get('aid')
		saverecord.amenu=request.POST.get('amenu')
		saverecord.aamount=request.POST.get('aamount')
		
		
		saverecord.save()
		
		#messages.success(request, 'record inserted successfully!!..')
		return render(request, 'user.html')
	else:
		res1=carta.objects.all()
		res2=alacartaorder.objects.all()
		return render(request, 'adminpage.html', {'carta':res1, 'alacartaorder':res2})


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
@login_required
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
		if request.user.is_superuser:
			login(request, user)
			return render(request, 'support.html')
	else:
		return render(request, 'user.html')
@login_required
def adminlogin(request):
	form = AdminLoginForm(request.POST or None)
	
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		if request.user.is_superuser:
			login(request, user)
			messages.messages.success("New account created")
			return render(request, 'support.html')
	
	


@login_required
def user(request):
    return render(request, 'user.html')
def menupage(request):
    return render(request, 'menupage.html')
def adminpage(request):

    return render(request, 'adminpage.html')
def support(request):
	form = AdminLoginForm(request.POST or None)
	
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		if request.user.is_superuser:
			login(request, user)
			messages.messages.success("New account created")
			return render(request, 'demo.html')
	else:
    		return render(request, 'support.html')
def index(request):
    return render(request, 'index.html')


def showorder(request):

	return render_to_response('user.html', {'obj': models.OrderNow.objects.all()})

class PersonListView(ListView):
    model = EmpInsert2
    template_name = 'user.html'

def demo(request):
	result= OrderNow.objects.all()
	return render(request, 'adminhome.html', {'OrderNow':result})


def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_superuser:
				login(request, user)
# Redirect to index page.
				return HttpResponseRedirect("demo")
			else:
				return HttpResponse("myadmin")
	else:
		
# the login is a  GET request, so just show the user the login form.
		return render(request, 'myadmin.html')



def Contact(request):
	Contact_Form=ContactForm
	if request.method=='POST':
		form=Contact_Form(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name')
			contact_email = request.POST.get('contact_email')
			contact_content = request.POST.get('content')

			template=get_template('contact_form.txt')
			content = {
			'contact_name' : request.POST.get('contact_name'),
			'contact_email' : request.POST.get('contact_email'),
			'contact_content' : request.POST.get('contact_content'),
			}
			content=template.render(content)
			email=EmailMessage(
				"New Enquiry Email",
				content,
				"Creative Web" + '',
				['amitrajput111777@gmail.com'],
				headers={'Reply To': contact_email }
			)
		email.send()
		return redirect('home')
	return render(request, 'contact.html',{'form':Contact_Form})


def readexcel(request):
	if "GET" == request.method:
		return render(request, 'reader/excelread.html')
	else:
		excel_file=request.FILES["excel_file"]

	#You may put the file extension check here
	wb=openpyxl.load_workbook(excel_file)

	# getting all sheets
	sheets = wb.sheetnames
	print(sheets)

	#getting a particular sheet by name
	#Read School Worksheet
	schoolworksheet = wb["School Tiffin"]
	#print(schoolworksheet)

	#excel_data=list()
	#Iterate and get values from each cell
	for rowno, rowval in enumerate(schoolworksheet.iter_rows(min_row=2, max_row=schoolworksheet.max_row),start=2):
		row_data = list()
		for cell in rowval:
			row_data.append(str(cell.value))
		print(row_data)
	#excel_data.append(row_data)

	#Read Office Worksheet
	officeworksheet = wb["Office Tiffin"]
	#print(officeworksheet)

	#excel_data=list()
	#Iterate and get values from each cell
	for rowno, rowval in enumerate(officeworksheet.iter_rows(min_row=2, max_row=officeworksheet.max_row),start=2):
		row_data = list()
		for cell in rowval:
			row_data.append(str(cell.value))
		print(row_data)
	#excel_data.append(row_data)

	#Read Lunch Worksheet
	lunchworksheet = wb["Lunch Tiffin"]
	#print(lunchworksheet)

	#excel_data=list()
	#Iterate and get values from each cell
	for rowno, rowval in enumerate(lunchworksheet.iter_rows(min_row=2, max_row=lunchworksheet.max_row),start=2):
		row_data = list()
		for cell in rowval:
			row_data.append(str(cell.value))
		print(row_data)
	#excel_data.append(row_data)

	#Read Dinner Worksheet
	dinnerworksheet = wb["Dinner Tiffin"]
	#print(dinnerworksheet)

	excel_data=list()
	#Iterate and get values from each cell
	for rowno, rowval in enumerate(dinnerworksheet.iter_rows(min_row=2, max_row=dinnerworksheet.max_row),start=2):
		row_data = list()
		for cell in rowval:
			row_data.append(str(cell.value))
		print(row_data)
		excel_data.append(row_data)
		return render(request,'reader/excelread.html',{"excel_data":excel_data})