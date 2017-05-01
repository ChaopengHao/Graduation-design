#coding=utf-8
from django.shortcuts import render
from models import User, Address, City
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'index.html')


def book_info(request):
    return render(request, 'bookinfo.html')


def cart(request):
    return render(request, 'cart.html')


def login(request):
    return render(request, 'login.html')


def order(request):
    return render(request, 'order.html')


def order_info(request):
    return  render(request, 'orderinfo.html')


def register(request):
    isRegistered = False
    isUserExisted = False
    error = None
    if request.method == 'POST':
        if 'name' in request.POST:
            users = User.objects.filter(name=request.POST['name'])
            if users:
                isUserExisted = True
                error = "注册失败"
            else:
                new_city = City(city=request.POST['address'])
                new_city.save()
                new_address =Address(address=request.POST['address'], city=new_city)
                new_address.save()
                new_user = User(name=request.POST['name'], password=request.POST['password'],
                                email=request.POST['email'], sex=request.POST['sex'],
                                address=new_address, phone=request.POST['phone'],
                                age=request.POST['age'], active=True,
                                )
                new_user.save()
                isRegistered = True
    context = {'isRegistered': isRegistered, 'isUserExisted': isUserExisted, 'error': error}
    print context
    return render(request, 'register.html', context)


def user_info(request):
    return  render(request, 'userinfo.html')