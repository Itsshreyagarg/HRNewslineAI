from django.urls import path
from . import views
from .views import LoginAPI, RegisterAPI
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('create-hrnews/', views.create_hrnews, name='create_hrnews'),
    path('sign_up/', views.sign_up, name='sign_up'),

    path('logout/', views.logout_view, name='logout'),
    path('hr_directory/<int:id>/', views.hr_detail, name='hr-detail'),
    path('hr_directory/', views.hr_list, name='hr_list'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),

    # Add other paths as needed
]


