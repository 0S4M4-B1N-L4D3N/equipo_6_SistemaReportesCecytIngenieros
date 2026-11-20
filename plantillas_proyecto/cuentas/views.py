from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistroUsuarioForm

class RegistroView(CreateView):
  form_class = RegistroUsuarioForm
  template_name = 'registration/registro.html'
  success_url = reverse_lazy('login')
@login_required
def solo_para_usuarios(request):
  return render(request, 'protegido.html')