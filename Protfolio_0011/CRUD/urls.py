from django.urls import path
from . import views

urlpatterns = [
    path('createUsers/',views.createUserViews,name='createUser'),
    path('showUsers/',views.showUserViews),
    path('login/',views.loginUserView,name='loginUser'),
    path('logout/',views.logOutUser,name='loginUser'),
    path('iupdate/',views.updateUserView),
]
