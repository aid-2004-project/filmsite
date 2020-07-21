from django.shortcuts import render


def f404_view(request):
    return render(request,"f04.html")