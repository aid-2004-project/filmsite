from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from user.models import History

# def check_logging(fn):
#     def wrap(request, *args, **kwargs):
#         #检查登录
#         if 'username' not in request.session or 'uid' not in request.session:
#             # #检查Cookies
#             # c_username = request.COOKIES.get('username')
#             # c_uid = request.COOKIES.get('uid')
#             # if not c_username or not c_uid:
#                 #肯定没登录
#             return HttpResponseRedirect('/user/')
#         else:
#             #回写session
#             request.session['username'] = c_username
#             request.session['uid'] = c_uid
#         return fn(request, *args, **kwargs)
#     return wrap


# Create your views here.



def center_view(request):
    # if request.method == "GET":
        # user_id = request.session.get('uid')
        # return render(request, 'usercenter/userCenter.html', locals())
    if "username" in request.session:
        username = request.session["username"]
        uid = request.session["uid"]
        bks = History.objects.filter(user_id=uid).values('film__filmname', 'film__id', 'film__created_time')
        paginator = Paginator(bks, 4)
        cur_page = request.GET.get('page', 1)  # 得到默认的当前页
        page = paginator.page(cur_page)
        return render(request, "usercenter/userCenter.html", locals())
    else:
        return HttpResponseRedirect("/index/")


def center_logout_view(request):
    return HttpResponseRedirect("/logout/")
