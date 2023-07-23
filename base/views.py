from django.shortcuts import render
from django.db.models.functions import Lower

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
    # also sort the books according to the publication year
    #use (-publication_year) for descending order
    books =  Book.objects.order_by('publication_year')
    books_data = [{'title': book.title, 'author': book.author,'publication_year':book.publication_year} for book in books]


    # Cache the data for 2 minutes (120 seconds)
    cache.set('cached_books', books_data, timeout=120)

    return JsonResponse(books_data, safe=False)

#Sorting by Multiple Fields
def sortMultipleBooks(request):
    books = Book.objects.order_by('author', '-publication_year')
    books_data = [{'title': book.title, 'author': book.author,'publication_year':book.publication_year} for book in books]
    return JsonResponse(books_data,safe=False)


#Sorting with Case-Insensitive Order:
def case_insensitive_sorting(request):
    books = Book.objects.order_by(Lower('title'))
    books_data = [{'title': book.title, 'author': book.author,'publication_year':book.publication_year} for book in books]
    return JsonResponse(books_data,safe=False)





