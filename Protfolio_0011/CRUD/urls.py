from django.urls import path
from . import views

urlpatterns = [
    path('createUsers/',views.createUserViews,name='createUser'),
    path('showUsers/',views.showUserViews,name='userDashboard'),
    path('login/',views.loginUserView,name='loginUser'),
    path('logout/',views.logOutUser,name='loginUser'),
    path('update/',views.updateUserView,name='updateUser'),
    path('changePass/',views.passChangeView,name='passchange'),
]
