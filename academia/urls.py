from .views import IndexView
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', include('academia_django.urls'))
]
