from django.contrib import admin
from .models import Emp,Testimonial


class EmpAdmin(admin.ModelAdmin):
	list_display=('name','working','emp_id','phone','address')
	list_editable=('emp_id','phone')
	search_fields=('name','phone')


admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)



