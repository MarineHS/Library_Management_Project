from django.shortcuts import render, get_object_or_404
from .models import Book

# Search for author or title in the Book database
def book_search(request):
    query = request.GET.get('q', '')  
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request, 'Catalog/book_search.html', {'books': books, 'query': query})

def book_details(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    return render(request, 'Catalog/book_details.html', {'book': book})