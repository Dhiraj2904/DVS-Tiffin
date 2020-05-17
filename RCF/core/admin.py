from django.contrib import admin
from RCF.core.models import Orders, UpdateTiffin, OrderNow, EmpInsert
from django.contrib.auth.models import Group
import csv
from django.http import HttpResponse

def actions1(modelAdmin, request, queryset):

	meta = modelAdmin.model._meta
	field_names = [field.name for field in meta.fields]

	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
	writer = csv.writer(response)

	writer.writerow(field_names)
	for obj in queryset:
		row = writer.writerow([getattr(obj, field) for field in field_names])
	return response
actions1.short_description='Export to CSV'

def button(self, obj):
	return format_html('<a  href="{0}" class="button">Profile Link</a>&nbsp;',obj.button)
button.short_description = 'Action'
button.allow_tags = True

class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['order_id', 'contents', 'orderdate', 'custname', 'amount'] 
    list_display_links= None
    list_per_page=5
    actions=[actions1,]
    can_update=True

class updatetiff(admin.ModelAdmin):
	list_display=['sub_id', 'tiff_id', 'sname', 'samount']
	list_display_links=None
	list_per_page=5
	actions=[actions1,]

class OrderAdmin(admin.ModelAdmin):
    
    list_display = ['tiffin_type', 'subtiffin_type', 'from_date', 'to_date', 'total_amount'] 
    list_display_links= None
    list_per_page=10
    actions=[actions1,]
    can_update=True


admin.site.site_header='Welcome Admin'
admin.site.register(UpdateTiffin, updatetiff)
admin.site.register(OrderNow, OrderAdmin)
admin.site.unregister(Group)
admin.site.register(Orders, ProductAdmin)
admin.site.index_title='Chapati Roti Administrator'
