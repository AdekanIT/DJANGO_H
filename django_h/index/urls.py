from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('regist', views.regist_form),
    path('states', views.states)
]