from django.forms import ModelForm
from .models import Order,Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Createform(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
class CreateCustomerform(ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'
        exclude = ['user']
class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']
class setting(ModelForm):
    class Meta:
        model = Customer
        fields='__all__'
        exclude = ['user']
