from . import views
from django.urls import path,include
from .models import StoreDetails
urlpatterns=[
    path('',views.home_page),
    path('stores/create',views.create_store),
    path('store/<int:store_id>',views.get_store_details),
    
]