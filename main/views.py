from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.all()
    # books = Book.objects.order_by('-id')[:3]
    # books = Book.objects.filter(author='ГОСТ')
    # books = Book.objects.filter(id__gt=2)
    # books = Book.objects.filter(id__lt=5)
    return render(request, 'main/index.html', {'title': 'Главная страница', 'books': books})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')

