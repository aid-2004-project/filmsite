from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
import hashlib


# Create your views here.
def index_view(request):
    filminfos = FilmInfo.objects.order_by("-id")[0:5]
    if request.method == "GET":
        if "username" in request.session:
            username = request.session["username"]
            uid = request.session["uid"]
            return render(request, 'user/index.html', locals())
        return render(request, 'user/index.html',locals())
    elif request.method == "POST":
        try:
            username = request.POST["username"]
            pwd = request.POST["pwd"]
        except Exception as e:
            print("input error is %e" % e)
            return HttpResponse("用户名或密码错误/为空")
        m = hashlib.md5()
        m.update(pwd.encode())
        password = m.hexdigest()
        if request.POST.get("register"):
            try:
                user = User.objects.create(username=username, password=password)
            except Exception as e:
                print("--create error is %s" % e)
                return HttpResponse("用户名已存在")
            request.session["username"] = user.username
            request.session["uid"] = user.id
            return render(request, 'user/index.html', locals())

        elif request.POST.get("login"):
            try:
                old_user = User.objects.get(username=username, password=password)
            except Exception as e:
                print("login error is %s" % e)
                return HttpResponse("用户名或密码错误")

            resp = HttpResponse("")
            request.session["uid"] = old_user.id
            request.session["username"] = username
            resp.set_cookie("username", username, 3 * 24 * 3600)
            resp.set_cookie("uid", old_user.id, 3 * 24 * 3600)
            return render(request, 'user/index.html', locals())


def logout_view(request):
    resp = HttpResponseRedirect("/index")
    request.session.clear()
    return resp
