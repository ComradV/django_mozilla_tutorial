from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Book, Author, BookInstance, Genre

def empty_view(request):
    return HttpResponse('This is empty now.')

def empty_view_id(request, id):
    return HttpResponse(f'This is empty now. ID: {id}')

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()

    num_genres = Genre.objects.all().count()

    num_books_with_word_book = Book.objects.filter(title__contains="book").count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_with_word_book': num_books_with_word_book,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)