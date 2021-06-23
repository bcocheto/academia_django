from .views import IndexView, FuncView, FichaView, ClientView, DadosAcademiaView
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cliente/', ClientView.as_view(), name='client'),
    path('func', FuncView.as_view(), name="func"),
    path('ficha/<int:id>/', FichaView.as_view(), name="ficha"),
    path('dados-academia', DadosAcademiaView.as_view(),name='dados-academia'),
    path('', include('academia_django.urls'))
]
