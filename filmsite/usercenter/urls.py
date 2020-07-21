from django.urls import path

from usercenter import views

urlpatterns = [
    path("", views.center_view),
    path("logout", views.center_logout_view),
]
