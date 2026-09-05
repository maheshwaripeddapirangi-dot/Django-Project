from django.shortcuts import render
from django.http import JsonResponse
from .models import StoreDetails
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
def home_page(req):
     StoreDetails.objects.create(
          store_name='Electronic_Store',
          store_address='Hyderabad',
          no_of_rooms=3,
          
    )
     return JsonResponse({'status':'Welcome to the page'})
@csrf_exempt
def create_store(req):
     if req.method=="POST":
          print(req.body)
          data=json.loads(req.body)
          print(data)
          s1=StoreDetails.objects.create(
               store_name=data['store_name'],
               store_address=data['store_address'],
               no_of_rooms=data['no_of_rooms'],
          )
          print(s1)
          return JsonResponse({'status':'success','store_id':s1.id})
     return JsonResponse({'status':'status failed','store_id':s1.id})
def get_store_details(req,store_id):
     store_details=get_object_or_404(StoreDetails,id=store_id)
     res={}
     res['id']=store_details.id
     res['store_name']=store_details.store_name
     res['store_address']=store_details.store_address
     res['store_no_of_rooms']=store_details.no_of_rooms
     return JsonResponse(res)
     
     # store_details=StoreDetails.objects.get(id=store_id)
     # print(store_details)
     # print(store_details.store_name,store_details.no_of_rooms)
     # res={}
     # res['id']=store_details.id
     # res['store_name']=store_details.store_name
     # res['store_address']=store_details.store_address
     # res['store_no_of_rooms']=store_details.no_of_rooms
     # return JsonResponse(res)



# Create your views here.
