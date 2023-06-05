from django.urls import path

from .views import *

urlpatterns = [
    path('', market, name="market"),
    path('<slug:cardname>/', card_info)
]