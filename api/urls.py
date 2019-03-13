from django.urls import path, include

from . import views

app_name = 'api'

from . import views

urlpatterns = [
    path('', views.Tasks.as_view()),
    # path('<int:pk>/', views.DetailTodo.as_view()),
    # path('login/', views.login),
    path('rest-auth/', include('rest_auth.urls')),
]