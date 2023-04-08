from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name="home"),
    path('markAttendance', views.markAttendance,name="markAttendance"),
    path('registerStudent', views.registerStudent,name="registerStudent"),
    path('confirmAttendance', views.confirmAttendance,name="confirmAttendance"),
    path('trackAttendance', views.trackAttendance,name="trackAttendance"),
]
