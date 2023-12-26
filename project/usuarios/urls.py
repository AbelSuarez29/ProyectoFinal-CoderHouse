from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "usuarios"

urlpatterns = [
    path("", views.home, name = "index"),
    path("registro/", views.registro_view, name="registro"),
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"),
]