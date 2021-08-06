from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),

]
