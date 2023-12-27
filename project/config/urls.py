from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('blog/', include("blog.urls")),
    path('usuarios/', include("usuarios.urls")),
]

url_patterns_for_media = static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns = urlpatterns + url_patterns_for_media