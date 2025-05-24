from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # ESTO ES CLAVE para /accounts/login/
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("sitiologin.urls"))  # Tus URLs de la app sitiologin
]
