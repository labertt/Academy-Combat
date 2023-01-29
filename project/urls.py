from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('usuarios.urls')),
    path('aluno/', include('aluno.urls')),
    path('mensalidade/', include('mensalidade.urls')),
    path('presenca/', include('presenca.urls')),
]
