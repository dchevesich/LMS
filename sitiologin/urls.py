from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.home_logeado_view, name="dashboard_usuario"),
]
