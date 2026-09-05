from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.home_page),
    path('get_user/<int:input_id>',views.get_user),
    path('create_user/',views.create_user),
    path('get_all_user/',views.get_all_user),
    path('update_user/<int:input_id>',views.update_user),
]