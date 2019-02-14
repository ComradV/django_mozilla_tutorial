from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from catalog.models import Book, Author, BookInstance, Genre

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author

class BookDetailView(generic.DetailView):
    model = Book

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    # context_object_name = 'my_book_list'   # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location    

def empty_view(request):
    return HttpResponse('This is empty now.')

def empty_view_id(request, params):
    return HttpResponse(f'This is empty now. ID: {params.id}')

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