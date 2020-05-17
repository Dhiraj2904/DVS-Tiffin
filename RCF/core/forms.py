from django import forms
from django.contrib.auth import login,authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from RCF.core.models import societyname


USER_TYPE_CHOICES = (
('school', 'School Tiffin'),
('office', 'Office Tiffin'),)


class RF(UserCreationForm):
	society=forms.CharField(required=True)
	confirm_password=forms.CharField(required=True)

	class Meta:
		model=User
		fields = (
			"username",
			"email",
			"password",
			"confirm_password",
			"society",
		)
	def save(self,commit=True):
		user=super(RF, self).save(commit=False)
		user.society=self.cleaned_data.get('society')

		if commit:
			user.save()
		return user


User = get_user_model()

class RegisterForm(forms.ModelForm):
	society=forms.CharField(required=True)
	class Meta:
		model = User
		fields = [
			"username",
			"email",
			"password",
			"confirm_password", 
			"society",
		]
	username = forms.CharField()
	email = forms.EmailField(label = "Email")
	password = forms.CharField(widget = forms.PasswordInput)
	confirm_password = forms.CharField(widget = forms.PasswordInput)
	society = forms.ModelChoiceField(queryset= societyname.objects.all(), label = "Select your Society")


	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"username"})
		self.fields['email'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"email"})
		self.fields['society'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"first_name"})
		self.fields['confirm_password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"confirm_password"})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"password"})
		


	def clean(self, *args, **keyargs):
		email = self.cleaned_data.get("email")
		confirm_password = self.cleaned_data.get("confirm_password")
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		society = self.cleaned_data.get("first_name")

		if password != confirm_password:
			raise forms.ValidationError("Passwords do not match")
		
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Email is already registered")

		username_qs = User.objects.filter(username=username)
		if username_qs.exists():
			raise forms.ValidationError("User with this username already registered")
		
		#you can add more validations for password

		if len(password) < 8:	
			raise forms.ValidationError("Password must be greater than 8 characters")


		return super(RegisterForm, self).clean(*args, **keyargs)



class UsersLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput,)

	def __init__(self, *args, **kwargs):
		super(UsersLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"username"})
		self.fields['password'].widget.attrs.update({
		    'class': 'form-control',
		    "name":"password"})

	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError("This user does not exists")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("User is no longer active")

		return super(UsersLoginForm, self).clean(*args, **keyargs)




