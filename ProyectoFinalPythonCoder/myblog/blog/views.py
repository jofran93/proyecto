# blog/views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Blog

@method_decorator(login_required, name='dispatch')
class AboutView(TemplateView):
    template_name = 'blog/about.html'

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog-list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('blog-list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('blog-list')
