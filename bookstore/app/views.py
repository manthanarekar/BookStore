from django.shortcuts import render,redirect
from .models import Books

# Create your views here.
def index(req):
    allbooks = Books.objects.all()
    print(allbooks)

    #  Adding Table data 
    # b = Books.objects.create(bookid=107,title='mongo',author='mm',category='database',price=3000,qty=114,dop='2023-08-25',photo=None)
    # b.save()

    # Updating Table Data
    # b = Books.objects.get(bookid=107)
    # b.author = 'Mayur k'
    # b.save()

    # Update using filter command
    # b = Books.objects.filter(bookid = 117).first()
    # b.author = 'manoj kumar'
    # b.save()
    context = {'allbooks':allbooks}
    return render(req,"index.html",context)


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password 
def signin(req):
    if req.method == 'POST':
        uemail = req.POST.get('uemail')
        upass = req.POST.get('upass')
        # uname = req.POST.get('uname')
        print(uemail,upass)
        # userdata = User.objects.filter(email=uemail,password=upass)
        # userdata = authenticate(email=uemail,password=upass)
        # print('USerdata :',userdata)
        # chk = User.objects.filter(username=uname,email=uemail)
        try:
            checkemail = User.objects.get(email=uemail)
            # print('chk :',chk)
            if checkemail.check_password(upass):
                login(req,checkemail)
                return render(req,'dashborad.html')
            else:
                messages.error(req,"Invalid email or password")
                return render(req,"signin.html")  
        except User.DoesNotExist:
            messages.error(req,"email id not exists")
            return render(req,'signin.html')
    else:
        
        return render(req,"signin.html")


from django.contrib import messages
from django.contrib.auth.models import User

def signup(req):
    print(req.method)
    if req.method == 'POST':
        uname = req.POST.get('uname')
        uemail = req.POST.get('uemail')
        upass = req.POST.get('upass')
        ucpass = req.POST.get('ucpass')
        print(uname,uemail,upass,ucpass)
        user = User.objects.values_list('username',flat=True)
        checkmail = User.objects.values_list('email',flat=True)
        print(checkmail)


        if upass != ucpass:
            # For Developer costumization 
            # errmsg = "
            # context = {'errmsg':errmsg}
            # return render(req,'signup.html',context)

            messages.error(req,"Password and confirm password doesn't match. Try again")
            return render(req,"signup.html")
        
        elif uname == upass:
            messages.error(req,"Username and password be different")
            return render(req,"signup.html")    

        elif uname in user:
               messages.error(req,"User name alrady exsits")
               return render(req,"signup.html")
             
        elif uemail in checkmail:
            messages.error(req,"email alrady exsits")
            return render(req,"signup.html")     
        
        else:
            newuser = User.objects.create(username=uname,email=uemail,password=upass)
            newuser.set_password(upass)
            newuser.save()

            messages.error(req,"Registration done successfully!")
            return render(req,"signin.html")
    
    else:
        return render(req,"signup.html")

def contact(req):
    return render(req,"contact.html")

def about(req):
    return render(req,"about.html")

from datetime import datetime

def DTldemo(req):
    name = 'Manthan'
    password = 'admin'
    author = ['pp','jj','cc']
    student = {1:{'name':'pooja','issuedbook':'python'},2:{'name':'Raj','issuedbook':'Java'}}
    context = {'name':name , 'DateTime' : datetime.now(),'hour':datetime.now().hour,'password':password,'author':author , 'student': student }
    return render(req,'DTldemo.html',context)

def dashborad(req):
    return render(req,"dashborad.html")

def userlogout(req):
    logout(req)
    return redirect('/')