from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path("signup", views.signup_user, name="signup"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),



]