from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name = "index"),
    path("about/", views.about, name="about"),
    path('', views.index, name='index'),
    path('guardar_noticia/', views.guardar_noticia, name='guardar_noticia'),
    path('buscar_noticia/', views.buscar_noticia, name='buscar_noticia'),
]
