from django.urls import path, include
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logot_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
]
