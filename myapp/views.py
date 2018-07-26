from django.shortcuts import render
from django.shortcuts import HttpResponse
from urllib.request import urlopen
from myapp import models
import uuid
import hashlib

# Create your views here.

def demo(request):
    wz = 'http://www.pythonscraping.com/pages/warandpeace.html'
    wz = 'http://www.pythonscraping.com/pages/page3.html'
    html = urlopen(wz).read()
    print(html)
    return HttpResponse(html)
    # return HttpResponse("<h1 style = 'color:red'>hello Python!!!</h1>")

def login(request):
    return render(request, 'login.html')

user_list = []

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('pass', None)
        if password != '666':
            return HttpResponse("<h1 style = 'color:red'>密码错误!!!</h1>")
        temp = {'username': username, "pass": password}
        user_list.append(temp)
    return render(request, 'index.html', {'data': temp})

def addhtml(request):
    user_list = models.user.objects.all()
    return render(request, 'userDemo.html', {'data': user_list})

def addUser(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        pwd = request.POST.get('pwd', None)
        h = hashlib.md5()
        h.update(bytes(pwd + '中国', encoding='utf-8'))
        models.user.objects.create(id=uuid.uuid1(), name=name, pwd=h.hexdigest())
    return HttpResponse('添加成功!!!')

def dele(request):
    id = request.POST.get('id', None)
    models.user.objects.filter(id=id).delete()
    return HttpResponse('删除成功!')