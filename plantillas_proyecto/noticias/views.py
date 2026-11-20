from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
  model = Post
  template_name = 'noticias/post_list.html'
  context_object_name = 'posts'
  
class PostDetailView(DetailView):
  model = Post
  template_name = 'noticias/post_detail.html'
class PostCreateView(CreateView):
  model = Post
  fields = ['titulo', 'contenido']
  template_name = 'noticias/post_form.html'
  success_url = reverse_lazy('post_list')
class PostUpdateView(UpdateView):
  model = Post
  fields = ['titulo', 'contenido']
  template_name = 'noticias/post_form.html'
  success_url = reverse_lazy('post_list')
class PostDeleteView(DeleteView):
  model = Post
  template_name = 'noticias/post_confirm_delete.html'
  success_url = reverse_lazy('post_list')