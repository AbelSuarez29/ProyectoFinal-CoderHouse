from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("", views.home, name = "index"),
    path("registro/", views.registro_view, name="registro"),
]