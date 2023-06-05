from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def forum(request):
    if request.method=='POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                ForumMessages.objects.create(**form.cleaned_data, user=request.user)
                return (redirect('/forum'))
            except Exception as e:
                print(e)
    coments = ForumMessages.objects.all()
    form = AddPostForm()
    return render(request, 'forum.html', {"title":"Форум Supply",
                                          "coments" : coments[::-1],
                                          'form': form})
# Create your views here.
