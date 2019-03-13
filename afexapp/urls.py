from django.urls import path

from . import views

app_name = 'afexapp'

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('create_task/', views.save_task, name='save_task'),
    # path('', views.profile, name='profile'),
]