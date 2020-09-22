from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .form import Createform,CreateCustomerform,CreationUserForm,setting
from .models import *
from .filters import OrderFiter,CustomerFilter
from django.contrib.auth import authenticate,login,logout
from .decoration import unauthenticated_user,allowed_user,admin_only



@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def user(request):
    orders=request.user.customer.order_set.all()
    order_count=orders.count()
    Delivered=orders.filter(status ='DELIVERED').count()
    PENDING=orders.filter(status ='PENDING').count()
    context={'orders':orders,'order_count':order_count,'Delivered':Delivered,'PENDING':PENDING}
    return render(request,'content/userpage.html',context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def profilesetting(request):
    customer = request.user.customer
    form = setting(instance=customer)
    if request.method == 'POST':
        form = setting(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    return render(request,'content/setting.html',context)




@unauthenticated_user
def registration(request):
    form=CreationUserForm()
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request,'Account was created for  ' + username)
            return redirect('login')
    context={'form':form}
    return render(request,'content/register.html',context)
@unauthenticated_user
def Loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'user or password is incorrect')


    context={}
    return render(request,'content/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
@admin_only
def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    order_count=orders.count()
    Delivered=orders.filter(status ='DELIVERED').count()
    PENDING=orders.filter(status ='PENDING').count()
    customer_filter=CustomerFilter(request.GET,queryset=customers)
    customers=customer_filter.qs
    context={'customers':customers,'orders':orders,'order_count':order_count,'Delivered':Delivered,'PENDING':PENDING,'customer_filter':customer_filter}
    return render (request,'content/dashboard.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    order_count=orders.count()
    myfilter=OrderFiter(request.GET,queryset=orders)
    orders=myfilter.qs

    context={'customer':customer,'myfilter':myfilter,'orders':orders,'order_count':order_count}
    return render (request,'content/customer.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def product(request):
    return render (request,'content/product.html')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def CreateFrom(request,pk):
    orders=Order.objects.get(id=pk)
    form=Createform(instance=orders)
    if request.method == 'POST':
        form=Createform(request.POST,instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'content/update.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def Deleteorder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method == 'POST':
            order.delete()
            return redirect('/')

    context={'item':order}
    return render(request,'content/delete_form.html',context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def CreateOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customer,Order,fields=('product','status'),extra=10)
    customer=Customer.objects.get(id=pk)
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == "POST":
        formset=OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset,'customer':customer}
    return render(request, 'content/create_form.html', context)

# @login_required(login_url='login')
# @allowed_user(allowed_roles=['admin'])
# def CreateCustomer(request):
#     create=CreateCustomerform()
#     if request.method == "POST":
#         create = CreateCustomerform(request.POST)
#         if create.is_valid():
#             create.save()
#             return redirect('/')
#     context = {'create': create}
#     return render(request, 'content/createcustomer.html', context)
