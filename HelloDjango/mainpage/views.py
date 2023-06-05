from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from .utils import DataMixin


def index(request):
    return render(request, 'index.html', {"title": "Supply"})


def about(request):
    return render(request, 'about.html', {"title": "Supply о нас"})

def login(request):

    return render(request, 'login.html')

def user_page(request):
    users_list = OurUser.objects.all().filter(auth=True)
    return render(request, 'user.html',{"title": "Пользователи",
                                        "users_list": users_list})


class RegForm(CreateView):

    form_class = RegisterUserForm
    template_name = "register.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        OurUser.objects.create(user=self.request.POST["username"], auth=False)
        return reverse_lazy("login")


class LoginForm(LoginView):

    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        OurUser.objects.all().filter(user=self.request.user).update(auth=True)


        return reverse_lazy('home')

def logut_user(request):
    OurUser.objects.all().filter(user=request.user).update(auth=False)

    logout(request)

    return redirect('/')

def pageNotFound(request ,exception):
    return reverse_lazy("home")