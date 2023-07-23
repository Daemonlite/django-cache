# bookapi/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/books/', views.get_books, name='get_books'),
    path('api/multiple-sorting',views.sortMultipleBooks,name='multiple-sort'),
    path('api/case-insensitive',views.case_insensitive_sorting,name='case-insensitive')
]
