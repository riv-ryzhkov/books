from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def index(request):
    # books = Book.objects.all()
    books = Book.objects.order_by('-id')
    # books = Book.objects.order_by('-id')[:3]
    # books = Book.objects.filter(author='ГОСТ')
    # books = Book.objects.filter(id__gt=2)
    # books = Book.objects.filter(id__lt=5)
    return render(request, 'main/index.html', {'title': 'Главная страница', 'books': books})

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

