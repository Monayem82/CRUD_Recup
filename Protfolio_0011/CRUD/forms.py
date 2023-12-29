from typing import Any
from django import forms
from django.forms import ModelForm,widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

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