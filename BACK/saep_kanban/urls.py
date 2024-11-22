from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),  # Inclui as URLs do app
    path('api/auth/', include('djoser.urls')),  # URLs do Djoser
    path('api/auth/', include('djoser.urls.authtoken')),  # Autenticação por token
]
