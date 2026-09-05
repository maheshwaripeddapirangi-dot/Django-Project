from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializers import Users_Serializer
from .models import Users
import json
from django.views.decorators.csrf import csrf_exempt

def home_page(req):
    return JsonResponse({'status':'Project setup successfully'})

# GET ONE USER
def get_user(req,input_id):
    u1=Users.objects.get(id=input_id)
    # user_dict={}
    # user_dict['Name']=u1.name
    # user_dict['Phone Number']=u1.phone_number
    # user_dict['Role']=u1.role
    # user_dict['Address']=u1.address

    u1_json=Users_Serializer(u1)
    return JsonResponse(
        {
            'user_details':u1_json.data
        }
    )

# POST
@csrf_exempt
def create_user(req):
    # print(req.body)
    data=json.loads(req.body)
    # print(data)
    input_user=Users_Serializer(data=data)
    if input_user.is_valid():
        input_user.save()
        return JsonResponse(input_user.data,status=200)
    return JsonResponse(input_user.errors,status=400)
# Create your views here.

# READ MANY
def get_all_user(req):
    All_user=Users.objects.all()
    return JsonResponse(Users_Serializer(All_user,many=True).data,safe=False)

# PUT
@csrf_exempt
def update_user(req,input_id):
    u1=Users.objects.get(id=input_id)
    data=json.loads(req.body)
    up=Users_Serializer(u1,data=data,partial=False)
    if up.is_valid():
        up.save()
        return JsonResponse(up.data,status=200)
    return JsonResponse(up.errors,status=400)

# PATCH
@csrf_exempt
def update_user(req,input_id):
    u1=Users.objects.get(id=input_id)
    data=json.loads(req.body)
    up=Users_Serializer(u1,data=data,partial=True)
    if up.is_valid():
        up.save()
        return JsonResponse(up.data,status=200)
    return JsonResponse(up.errors,status=400)

