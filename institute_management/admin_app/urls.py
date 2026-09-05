from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('admin_int/',views.admin_dashboard,name='admin_dashboard'),
    path('create_student/',views.create_student,name='create_student'),
    path('remove_student/',views.remove_student,name='remove_student'),
    path('create_course/',views.create_course,name='create_course'),
]