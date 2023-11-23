# blog/urls.py
from django.urls import path
from .views import AboutView, BlogListView, BlogDetailView, register, user_login, user_logout

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('pages/', BlogListView.as_view(), name='blog-list'),
    path('pages/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
