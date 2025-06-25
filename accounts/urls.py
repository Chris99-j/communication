from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('adminpanel/', views.admin_dashboard, name='admin_dashboard'),
    path('', views.home, name='home'),  # Optional: add this to fix the 404 at /
]
