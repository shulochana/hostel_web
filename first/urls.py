from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path("login",views.login,name='login'),
    path("logout",views.logout, name='logout'),
    path("index", views.index, name='index'),
    path("table", views.table, name='table'),
    path("shar",views.shar,name='shar'),
    path("nel",views.nel,name='nel')

]