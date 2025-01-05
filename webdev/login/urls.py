from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('post-status', views.post_status, name='post-status'),
    path('shop/', views.shop, name="login"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('why_us/', views.why_us, name="why us"),
    path('contact/', views.contact, name='contact'),
]
