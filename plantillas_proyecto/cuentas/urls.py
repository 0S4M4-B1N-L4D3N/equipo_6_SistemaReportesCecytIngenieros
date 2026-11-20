from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistroView, solo_para_usuarios
urlpatterns = [
  path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('registro/', RegistroView.as_view(), name='registro'),
  path('protegido/', solo_para_usuarios, name='protegido'),
]