from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name = "index"),
    path("about/", views.about, name="about"),
    path("crear_videojuegos/", views.videojuegos_view, name="noticia_videojuegos"),
    path("crear_videojuegos/todos", views.videojuegos_todos_view, name="noticia-todos"),
    path("buscar_noticia", views.buscar_noticia, name="buscar")
]
