from django.urls import path
from . import views 

urlpatterns = [
   path('', views.employee_form, name='employee_form'),
   path('list/', views.employee_list, name='employee_list'),
 ]