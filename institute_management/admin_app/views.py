from django.shortcuts import render,redirect
from . models import Users,Courses
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# login_failed=False
login_name=None
login_role=None
login_status=False
def home_page(req):
    return render(req,'home.html')
def admin_dashboard(req):
    global login_name,login_role,login_status
    username=req.POST.get('username')
    password=req.POST.get('password')
    u1=Users.objects.filter(name=username,password=password,role='admin').exists()
    print(u1)
    if u1:
        login_name=username
        login_role='admin'
        login_status=True
        all_students=Users.objects.filter(role='student')
        return render(req,'admin_dashboard.html',{'students':all_students})
    else:
        # global login_failed
        # login_failed=True
        return redirect('/')
    return render(req,'admin_dashboard.html')
def create_student(req):
    if req.method=='POST':
        username=req.POST.get('username')
        phone_number=req.POST.get('phone_number')
        address=req.POST.get('address')
        password=req.POST.get('password')
        Users.objects.create(
            name=username,
            phone_number=phone_number,
            address=address,
            password=password,
            role='student'

        )
        
        return redirect('/admin_int')
    else:
        if login_status==True and login_role=='admin':
            return render(req,'create_student.html')
        else:
            return redirect('/')
def remove_student(req):
    if login_status==True and login_role=='admin':
        id = req.session.get("id")
        if id:
            Users.objects.filter(id=id).delete()
            req.session.flush()
        # return redirect("")
        return render(req,'remove_student.html')
    else:
        return redirect('/')
    # id = req.session.get("id")
    # if id:
    #     Users.objects.filter(id=id).delete()
    # req.session.flush()
    # return redirect("")
@csrf_exempt
def create_course(req):
    users_id=req.POST.get('users_id')
    courses_id=req.POST.get('courses_id')
    if Courses.objects.filter(id=courses_id).exists() and Users.objects.filter(id=users_id).exists():
        course=Courses.objects.get(id=courses_id)
        student=Users.objects.get(id=users_id)
        course.Students.add(student)
        course.save()
        students=course.students.all()
        for student in students:
            return student
        return JsonResponse({'status':'course_assigned'})
    elif not  Courses.objects.filter(id=courses_id).exists():
        return JsonResponse({'status':'Failed.....Invalid course id'})
    else:
        return JsonResponse({'status':'Association Failed.'})



# Create your views here.
