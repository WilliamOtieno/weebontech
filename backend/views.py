from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'backend/index.html')


def about(request):
    return render(request, 'backend/about.html')


def products(request):
    return render(request, 'backend/products.html')


def store(request):
    return render(request, 'backend/store.html')
