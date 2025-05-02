from django.shortcuts import render
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

def signin(req):
    return render(req,"signin.html")

def signup(req):
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