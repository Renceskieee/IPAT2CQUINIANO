from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
]