from django.urls import path,include
from utilizatori import views


urlpatterns=[
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("profil/", views.profil, name="profil"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("password_change/", views.change_password, name="password_change"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("reset/<uidb64>/<token>", views.password_reset_confirm, name="reset"),
    path("materii_an1/", views.materii_an1, name="materii_an1"),
    path("materii_an2/", views.materii_an2, name="materii_an2"),
    path("materii_an3/", views.materii_an3, name="materii_an3"),

    ]