from django.shortcuts import render
from django.http import HttpResponseRedirect
from CRUD.forms import CreateUser,loginUser
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def createUserViews(request):
    if request.method=='POST':
        frm=CreateUser(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm=CreateUser()
    return render(request,'CRUD/userCreate.html',context={'form':frm})

# def showUserViews(request):
#     users=CreateUser.objects.all()
#     return render(request,'CRUD/showUser.html',context={"users":users})

def loginUserView(request):
    if request.method=='POST':
        frm=loginUser(request=request,data=request.POST)
        if frm.is_valid():
            usern=frm.cleaned_data['username']
            passn=frm.cleaned_data['password']
            user=authenticate(username=usern,password=passn)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/crud/createUsers/')
    else:
        frm=loginUser()
    return render(request,'CRUD/loginUser.html',context={'user':frm})