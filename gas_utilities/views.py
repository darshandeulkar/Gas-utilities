from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def login(request):
    if request.method=="POST":
        username = request.POST.get('name')
        password = request.POST.get('password1')
        
        
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            # request.session['Stud_id'] = user.userinfo.Stud_id
            return render(request, 'login.html')
        else:
            # messages.error(request, 'valid username or password')
            return render (request,'index.html')
        

def register(request):
    if request.method == "POST":
        # roll = request.POST.get('rollno')  Mayuri321
        username = request.POST.get('name')
        email = request.POST.get('email')
        Password = request.POST.get('password1')
        Password1 = request.POST.get('password2')

        
        if Password != Password1:
            messages.error(request, "Passwords do not match")
            return redirect('/')
        
        myuser = User.objects.create_user(username,email, Password)
        myuser.save()

        
        # user.save();
        return render (request,'index.html')

from .models import ServiceRequest

def service_request(request):
    if request.method == 'POST':
        service_type = request.POST.get('serviceType')
        description = request.POST.get('description')
        attachment = request.FILES.get('attachment')
        service_request = ServiceRequest(
            service_type=service_type,
            description=description,
            attachment=attachment
        )
        service_request.save()
        
        # form = ServiceRequest(request.POST, request.FILES)
    
        messages.success(request, 'Your service request has been sent successfully!')
        return render (request,'login.html')
            # Redirect to a success page or home page
            # return redirect('home')


def serviceprologin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')

        if uname == "servicepro" and password == "servicepro":
            return render(request,'servicepro.html')

def showrequest(request):
    if request.method == "POST":
       requests = ServiceRequest.objects.all()
    return render(request,'servicepro.html',{"requests":requests})

