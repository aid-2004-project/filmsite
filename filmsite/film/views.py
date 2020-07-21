from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from user.models import *
import hashlib


# Create your views here.
def messageboard_view(request):
    if request.method == "GET":
        bks = MessageBoard.objects.filter()
        print(bks)
        paginator = Paginator(bks, 10)
        cur_page = request.GET.get('page', 1)  # 得到默认的当前页
        page = paginator.page(cur_page)
        return render(request, 'user/play.html', locals())
    elif request.method == "POST":
        content = request.POST['content']
        if content:
            try:
                content = MessageBoard.objects.create(content=content, user_id=1, film_id=1)
            except Exception as e:
                print('create error is %s' % (e))
                return HttpResponse('Something is wrong!')
        else:
            return HttpResponseRedirect('/messageboard')
        return HttpResponseRedirect('/messageboard')


def play_view(request, film_id):
    try:
        film = FilmInfo.objects.get(id=film_id)
    except Exception as e:
        print(f"----film error is {e}")
        # raise Http404
        return HttpResponse("404")
    if "username" in request.session:
        username = request.session["username"]
        uid = request.session["uid"]
    return render(request, "film/play.html",locals())
