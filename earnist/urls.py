from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('register/', views.register, name='register'),
    path('add/', views.add_record, name='add_record'),
    path('update/<int:pk>', views.update_record, name='update_record'),
    path('remove/<int:pk>', views.delete_record, name='delete_record'),
    path('logout/', views.logout_user, name='logout'),
]