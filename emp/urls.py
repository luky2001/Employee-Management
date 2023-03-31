
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
  path("",home),
  path("home/",home),
  path("add/",add_emp),
  path("delete/<int:emp_id>",delete_emp),
  path("update/<int:emp_id>",update_emp),
  path("do/<int:emp_id>",do_emp),
  path("testimonials/",testimonials),
 
   
]
