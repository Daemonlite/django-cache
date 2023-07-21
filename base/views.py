from django.shortcuts import render

# Create your views here.

from django.core.cache import cache
from django.http import JsonResponse
from .models import Book

def get_books(request):
    # Check if the data is already cached
    cached_books = cache.get('cached_books')
    if cached_books is not None:
        return JsonResponse(cached_books, safe=False)

    # If not cached, retrieve the books from the database
    books = Book.objects.all()
    books_data = [{'title': book.title, 'author': book.author} for book in books]

    # Cache the data for 20 minutes (1,200 seconds)
    cache.set('cached_books', books_data, timeout=1200)

    return JsonResponse(books_data, safe=False)
