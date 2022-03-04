from datetime import date
from datetime import datetime

from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *

from django.utils import timezone

# Create your views here.





def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")


def navigation(request):
    return render(request,"navigation.html")

def nav(request):
    return render(request,"admin_nav.html")


def login_admin(request):
    error = ""
    if request.method == "POST":
        u= request.POST['uname']
        p=request.POST['pwd']
        user= authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error = "yes"
    d={'error':error}
    return render(request,"login_admin.html",d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    p = Notes.objects.filter(status="pending").count()
    a = Notes.objects.filter(status="accept").count()
    r = Notes.objects.filter(status="reject").count()
    allc = Notes.objects.all().count()
    d={'p':p,'a':a,'r':r,'allc':allc}
    return render(request,"admin_home.html",d)


def user_logout(request):
    logout(request)
    return redirect('home')


def signup1(request):
    error=""
    if request.method=="POST":
        f= request.POST['fname']
        l= request.POST['lname']
        c= request.POST['contact']
        e= request.POST['email']
        p= request.POST['pwd']
        b = request.POST['branch']
        r = request.POST['role']
        try:
            user = User.objects.create_user(username= e,password=p,first_name=f,last_name =l)
            Signup.objects.create(user=user,contact=c,branch=b,role=r)
            error="no"
        except:
            error="yes"
    d={"error": error}
    return render(request,'signup.html',d)


def userlogin(request):
    error = ""
    if request.method=="POST":
        e = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=e, password=p)
        try:
            if user:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d ={'error': error}
    return render(request,"login.html", d)


def changepwd(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""

    if request.method == "POST":
        o = request.POST['old']
        n = request.POST['new']
        c = request.POST['confirm']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "no"
        else:
            error = "yes"
    d = {'error':error}
    return render(request,'changepwd.html',d)


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data': data,'user':user}
    return render(request,'profile.html',d)





def edit(request):
    if not request.user.is_authenticated:
        return redirect('profile')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    error=False
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        c = request.POST['contact']
        b = request.POST['branch']
        user.first_name =f
        user.last_name =l
        data.contact=c
        data.branch=b
        user.save()
        data.save()
        error=True
    d = {'data': data, 'user': user,'error': error}
    return render(request, 'edit.html', d)


def upload_notes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method=="POST":
        b = request.POST['branch']
        s = request.POST['subject']
        n= request.POST['notesfile']
        print(n)
        f = request.POST['filetype']
        d = request.POST['description']
        u = User.objects.filter(username=request.user.username).first()
        print(u)
        try:
            obj = Notes.objects.create(user=u,uploadingdate=datetime.now(),branch= b,subject=s,notesfile=n,filetype=f,description=d,status='pending')
            print(obj)
            obj.save()

            error = "no"
        except:
            error = "yes"
    d = {"error": error}
    return render(request,'upload_nodes.html',d)


def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('profile')
    user = User.objects.get(id=request.user.id)
    notes= Notes.objects.filter(user=user)
    d = {'notes': notes}
    return render(request,"view_mynotes.html",d)



def delete_mynotes(request,id):
    if not request.user.is_authenticated:
        return redirect('profile')
    notes= Notes.objects.get(id=id)
    notes.delete()
    return redirect('view_mynotes')



def view_user(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user = Signup.objects.all()
    d = {'user':user}
    return render(request,"view_user.html",d)



def delete_user(request,id):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    user= User.objects.get(id=id)
    user.delete()
    return redirect('view_user')



def pending(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes= Notes.objects.filter(status = "pending")
    print(notes)
    d = {'notes': notes}
    return render(request,"pending.html",d)


def assign_status(request,id):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.get(id=id)
    error=""
    if request.method == "POST":
        s = request.POST['status']
        print(s)
        try:
            notes.status = s
            notes.save()
            error = "no"
        except:
            error = "yes"
    d = {"error": error, "notes":notes}
    return render(request,'assign_status.html',d)


def accepted_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="accept")
    d = {'notes': notes}
    return render(request,"accepted_notes.html",d)


def rejected_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="reject")
    d = {'notes': notes}
    return render(request,"rejected_notes.html",d)


def all_notes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.all()
    d = {'notes': notes}
    return render(request,"all_notes.html",d)


def delete_notes(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    notes= Notes.objects.get(id=id)
    notes.delete()
    return redirect('all_notes')


def viewallnotes(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="accept")
    d = {'notes': notes}
    return render(request,"viewallnotes.html",d)










