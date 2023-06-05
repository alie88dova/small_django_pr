from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about),
    path('userpage/', user_page),
    path('login/',  LoginForm.as_view(), name="login"),
    path('register/', RegForm.as_view()),
    path('logout/', logut_user, name="logout")
]