from django.shortcuts import render, redirect
from django.http import HttpResponse as httpresponse
from .models import post

def home(request):
    posts = post.objects.all().order_by('-timestamp')[:5]
    return render(request, "login/index.html",{'posts':posts})

def login(request):
    return httpresponse('welcome to login.')

def post_status(request):
    if request.method == 'POST':
        username = request.POST.get('author')
        status_content = request.POST.get('status')

        post.objects.create(author=username, content=status_content)

        return redirect('home')
    
    return redirect('home')

def shop(request):
    return render(request, "login/shop.html",{})

def testimonial(request):
    return render(request, "login/testimonial.html",{})

def why_us(request):
    return render(request, "login/why.html",{})

def contact(request):
    return render(request, 'login/contact.html', {})
