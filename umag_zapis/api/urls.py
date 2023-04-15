from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),

    # Supplies
    path("supplies/", views.getSupplies, name="Supplies"),
    path("supplies/<str:pk>/", views.getSupply, name="Supply"),

    # Sales
    path("sales/", views.getSales, name="Sales"),
    path("sales/<str:pk>/", views.getSale, name="Sale"),

    # Report
    path("report/", views.getReport, name="Report"),


]
