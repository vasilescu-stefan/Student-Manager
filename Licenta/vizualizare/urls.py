from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="starting-page"),
    # path("login-user", views.login_request, name="login"),
    # path("register-user", views.register_request, name="register"),
    # path('cursuri/<int:pk>/change', views.change_cursuri, name='change_cursuri'),
    path('confirm-subiect/', views.confirm_subject_relation, name='confirm_subject_relation'),
    path('optional1/', views.optional1, name='optional1'),
    path('optional2/', views.optional2, name='optional2'),
    path('optional3/', views.optional3, name='optional3'),
    path('optional4/', views.optional4, name='optional4'),
    path('optional5/', views.optional5, name='optional5'),
    path('optional6/', views.optional6, name='optional6'),
    path('optional7/', views.optional7, name='optional7'),
]