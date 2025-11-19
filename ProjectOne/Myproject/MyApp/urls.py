from django.urls import path
from . import views



urlpatterns=[
    path('',views.Home,name='home'),
    path('create/',views.stdForm,name='stdForm'),
    path('addstd/',views.registStudent,name='regist_std'),
    path('fetch_std',views.retrievestd,name='fetch_std'),
    path('updatestd/<int:pk>',views.updatestd,name='updatestd'),
    path('deletestd/<int:pk>',views.deletestd,name='deletestd'),
    path('signup',views.userRegistration,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.log_out,name="logout"),
]




