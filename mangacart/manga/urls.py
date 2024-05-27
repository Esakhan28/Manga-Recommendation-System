from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('home/', views.members, name='members'),
    path('read/<path:title>/', views.read, name='read'),
    path('login/', views.admin_login, name = 'admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
]