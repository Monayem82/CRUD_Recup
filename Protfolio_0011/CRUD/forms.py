from typing import Any
from django import forms
from django.forms import ModelForm,widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm

class CreateUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CreateUser,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control lh-1'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
    

class loginUser(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(loginUser,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['class']='form-control'

class showUserDetiles(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']

class UpdateUserForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        #fields="__all__"
        fields=['username','email','first_name','last_name','is_staff','is_active','date_joined']

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UpdateUserForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control lh-1'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['date_joined'].widget.attrs['class']='form-control'

class passChangeForm(PasswordChangeForm):
    class Meta:
        model=User
        fields="__all__"
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(passChangeForm,self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class']='form-control lh-1'
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['class']='form-control'
