"""afex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import  url
from afexapp import views

urlpatterns = [
    path('affexapp/', include('afexapp.urls')),
    path('admin/', admin.site.urls),
    #  path('accounts/', include('django.contrib.auth.urls')), 
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    # path('<str:username>/', views.profile, name='profile'),
    # url(r'^(?P<username>[^/]+)/$', views.profile, name='user_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('api/v1/', include('api.urls')),
]
