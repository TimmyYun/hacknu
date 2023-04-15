from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getRoutes, name="routes"),

    # Supplies
    path('supplies/', views.getSupply, name="Artists"),
    # path('supplies/<str:pk>/', views.getSupplies, name="Artist"),


]
