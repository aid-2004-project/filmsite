from django.urls import path

from user import views

urlpatterns=[
    path('index/',views.index_view),
    # path('login/',views.login_view),
    # path('register/',views.reg_view),
    path('logout/',views.logout_view),
    # path('userCenter/',views.center_view),

]