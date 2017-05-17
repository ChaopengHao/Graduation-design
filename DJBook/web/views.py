#coding=utf-8
from django.shortcuts import render
from models import User, Address, City, JDBookItem, Order
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    if request.user.is_authenticated() :
        books = JDBookItem.objects.all()[:12]
        page = 1
        context = {"books": books, "page": page}
        return render(request, 'index.html', context)
    else:
        books = JDBookItem.objects.all()[:12]
        page = 1
        context ={"books":books, "page":page}
        return render(request, 'index.html', context)


def book_info(request, pk):
    print pk
    book = JDBookItem.objects.filter(id=pk)[0]
    print book
    context ={"book":book}
    return render(request, 'bookinfo.html', context)


@login_required(login_url="/login/")
def cart(request):
    return render(request, 'cart.html')


def user_login(request):
    errors = "登录失败！"
    if request.method == "POST":
        if 'username' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print user
            if user:
                login(request, user)
                print "login successed!"
                #return render(request, 'index.html')
                return HttpResponseRedirect('/')
            else:
                print "login failed！"
                return render(request, 'login.html', {'errors': errors})
        else:
            print "username unexisted！"
            return render(request, 'login.html', {'errors': errors})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url="/login/")
def order(request, pk=0):
    print "order"
    print pk
    if pk != 0:
        print pk
        book = JDBookItem.objects.filter(id=pk)[0]
        new_user = User.objects.filter(username=request.user)[0]
        new_order = Order(jd_goods=book, user=new_user)
        new_order.save()
        print 'baocun'
    new_user = User.objects.filter(username=request.user)[0]
    orders = Order.objects.filter(user=new_user)
    context = {"orders":orders}
    return render(request, 'order.html',context)


@login_required(login_url="/login/")
def order_info(request):
    return  render(request, 'orderinfo.html')


def register(request):
    isRegistered = False
    isUserExisted = False
    error = None
    if request.method == 'POST':
        if 'name' in request.POST:
            users = User.objects.filter(username=request.POST['name'])
            if users:
                isUserExisted = True
                error = "注册失败"
            else:
                new_city = City(city=request.POST['address'])
                new_city.save()
                new_address =Address(address=request.POST['address'], city=new_city)
                new_address.save()
                new_user = User.objects.create_user(username=request.POST['name'], password=request.POST['password'],
                                email=request.POST['email'], sex=request.POST['sex'],
                                address=new_address, phone=request.POST['phone'],
                                age=request.POST['age'], active=True,
                                )
                new_user.save()
                isRegistered = True
    else:
        print request.method
    context = {'isRegistered': isRegistered, 'isUserExisted': isUserExisted, 'error': error}
    print context
    return render(request, 'register.html', context)


@login_required(login_url="/login/")
def user_info(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            new_city = City(city=request.POST['address'])
            new_city.save()
            new_address = Address(address=request.POST['address'], city=new_city)
            new_address.save()
            new_user = User.objects.filter(username=request.POST['name']).update(username=request.POST['name'],
                                email=request.POST['email'], sex=request.POST['sex'],
                                address=new_address, phone=request.POST['phone'],
                                age=request.POST['age']
                                )
            isRegistered = True
            print "sucessed"
        elif 'new_password' in request.POST:
            new_user = User.objects.get(username=request.user)
            new_user.set_password(request.POST['new_password'])
            new_user.save()
            print "changed password sucessed"

    user = request.user
    users = User.objects.filter(username = user)
    print users[0]
    context={"username":users[0].username, "age":users[0].age, "sex":users[0].sex, "phone":users[0].phone, "email":users[0].email,
                "city":users[0].address.city.city, "address":users[0].address.address, "user":users[0]}
    print "haha"
    print context
    return  render(request, 'userinfo.html', context)


def index_change(request):
    if request.is_ajax():
        page = request.POST.get("page")
        page = int(page)
        #page = data.page
        books = JDBookItem.objects.all()[page*12:(page+1)*12]
        page += 1
        context = {"books": books, "page":page}
        return render(request, 'index.html', context)


def order_add(request,pk):
    book = JDBookItem.objects.filter(id=pk)[0]
    new_user = User.objects.filter(username=request.user)[0]
    new_order = Order(jd_goods=book, user=new_user)
    new_order.save()
    return render(request, 'orderinfo.html')

def order_delete(request,pk):
    Order.objects.filter(id =pk).delete()
    new_user = User.objects.filter(username=request.user)[0]
    orders = Order.objects.filter(user=new_user)
    context = {"orders":orders}
    return render(request, 'order.html',context)