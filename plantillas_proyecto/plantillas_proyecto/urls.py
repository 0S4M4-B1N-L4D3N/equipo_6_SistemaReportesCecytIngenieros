from django.contrib import admin
from django.urls import path
from noticias.views import home, detalle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('noticia/<int:id>/', detalle, name='detalle'),
]
