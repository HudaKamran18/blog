from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')


def services(request):
    return render(request, 'blog/services.html')


def works(request):
    return render(request, 'blog/works.html')


def blog(request):
    return render(request, 'blog/blog.html')


def contact(request):
    return render(request, 'blog/contact.html')