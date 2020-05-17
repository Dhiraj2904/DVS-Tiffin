from django.db import models
from django.db import connections
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


from django.conf import settings

User=get_user_model()


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]
    
class Orders(models.Model):
	order_id=models.IntegerField(primary_key=True)
	contents=models.CharField(max_length=100)
	orderdate=models.DateField(max_length=100)
	custname=models.CharField(max_length=100)
	amount=models.IntegerField()
	class Meta:
		db_table="reports"


class OrderNow(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	ordernow_id=models.IntegerField(primary_key=True)
	tiffin_type=models.CharField(max_length=100)
	subtiffin_type=models.CharField(max_length=100)
	from_date=models.DateField(max_length=100)
	to_date=models.DateField(max_length=100)
	total_amount=models.IntegerField()
	class Meta:
		db_table="ordernow"



class UpdateTiffin(models.Model):
	sub_id=models.IntegerField(primary_key=True)
	tiff_id=models.IntegerField()
	sname=models.CharField(max_length=100)
	samount=models.IntegerField()
	class Meta:
		db_table="updatetiffin"

class societyname(models.Model):
	soc_id=models.IntegerField(primary_key=True)
	soc_name=models.CharField(max_length=200)


	class Meta:
		db_table="society"

	def __str__(self):
		return self.soc_name




class EmpInsert(models.Model):
	ordernow_id=models.IntegerField(primary_key=True)
	created_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	tiffin_type=models.CharField(max_length=100)
	subtiffin_type=models.CharField(max_length=100)
	from_date=models.DateField(auto_now=False)
	to_date=models.DateField(auto_now=False)
	total_amount=models.IntegerField()
	class Meta:
		db_table=""

class EmpInsert2(models.Model):
	ttype=models.CharField(max_length=100)


class carta(models.Model):
	cid=models.IntegerField(primary_key=True)
	cmenu=models.CharField(max_length=100)
	sabji=models.CharField(max_length=100)
	sweets=models.CharField(max_length=100)
	camount=models.IntegerField()
	class Meta:
		db_table="menualcarta"
	


class orderdisplay(models.Model):
	oid=models.IntegerField(primary_key=True)
	tiffin_type=models.CharField(max_length=100)
	subtiffin_type=models.CharField(max_length=100)
	from_date=models.DateField(auto_now=False)
	to_date=models.DateField(auto_now=False)
	total_amount=models.IntegerField(max_length=100)
	class Meta:
		db_table="ordernow2"

class menudisplay(models.Model):
	mid=models.IntegerField(primary_key=True)
	Vegetarian=models.CharField(max_length=100)
	Mixed=models.CharField(max_length=100)
	Premium_Veg=models.CharField(max_length=100)
	Premium_Mixed=models.CharField(max_length=100)
	mdate=models.DateField()
	class Meta:

		db_table="mainmenu"

class otdisplay(models.Model):
	otid=models.IntegerField(primary_key=True)
	Vegetarian1=models.CharField(max_length=100)
	Mixed1=models.CharField(max_length=100)
	Premium_Veg1=models.CharField(max_length=100)
	Premium_Mixed1=models.CharField(max_length=100)
	odate1=models.DateField()
	class Meta:

		db_table="officetiffinmenu"

class ltdisplay(models.Model):
	ltid=models.IntegerField(primary_key=True)
	Vegetarian=models.CharField(max_length=100)
	Mixed=models.CharField(max_length=100)
	Premium_Veg=models.CharField(max_length=100)
	Premium_Mixed=models.CharField(max_length=100)
	ldate=models.DateField()
	class Meta:

		db_table="lunchtiffinmenu"

class dtdisplay(models.Model):
	dtid=models.IntegerField(primary_key=True)
	Vegetarian=models.CharField(max_length=100)
	Mixed=models.CharField(max_length=100)
	Premium_Veg=models.CharField(max_length=100)
	Premium_Mixed=models.CharField(max_length=100)
	ddate=models.DateField()
	class Meta:

		db_table="dinnertiffinmenu"