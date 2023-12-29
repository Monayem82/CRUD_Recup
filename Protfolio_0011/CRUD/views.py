from django.shortcuts import render
from django.http import HttpResponseRedirect
from CRUD.forms import CreateUser,loginUser,showUserDetiles,UpdateUserForm
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def createUserViews(request):
    if request.method=='POST':
        frm=CreateUser(request.POST)
        if frm.is_valid():
            frm.save()
            frm=CreateUser()
            return HttpResponseRedirect('/crud/login/')
    else:
        frm=CreateUser()
    return render(request,'CRUD/userCreate.html',context={'form':frm})

# Show User Detelis

def showUserViews(request):
    if request.user.is_authenticated:
        frm=showUserDetiles(instance=request.user)
        return render(request,'CRUD/showUserDashboard.html',context={"form":frm})
    else:
        return HttpResponseRedirect('/crud/login/')

# Valid Log in

def loginUserView(request):
    if request.method=='POST':
        frm=loginUser(request=request,data=request.POST)
        if frm.is_valid():
            usern=frm.cleaned_data['username']
            passn=frm.cleaned_data['password']
            user=authenticate(username=usern,password=passn)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/crud/showUsers/')
    else:
        frm=loginUser()
    return render(request,'CRUD/loginUser.html',context={'user':frm})

# log out 
def logOutUser(request):
    logout(request)
    return HttpResponseRedirect('/crud/login/')

# Update the User Informations

def updateUserView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm=UpdateUserForm(request.POST,instance =request.user)
            if frm.is_valid():
                frm.save()
                return HttpResponseRedirect('/crud/showUsers/')

        else:
            frm=UpdateUserForm(instance=request.user)
        return render(request,'CRUD/updateUser.html',context={"form":frm})
    else:
        return HttpResponseRedirect('/crud/login/')