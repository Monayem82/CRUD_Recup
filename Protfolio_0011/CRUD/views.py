from django.shortcuts import render
from CRUD.forms import CreateUser,loginUser


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
    user=loginUser()
    return render(request,'CRUD/loginUser.html',context={'user':user})