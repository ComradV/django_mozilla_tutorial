import uuid
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction)")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a language name (e.g. English)")

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}, {}'.format(self.title, self.isbn)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    class Meta:
        ordering = ['title','author']
    
    display_genre.short_description = 'Genre'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('Died', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def get_life_period(self):
        if self.date_of_birth :
            return f'{self.date_of_birth} - {self.date_of_death if self.date_of_death else "now"}'
        else:
            return '-'

    class Meta:
        ordering=['last_name','first_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Unique ID for this particular book across whole library'
    )
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(blank=True, null=True)
    LOAN_STATUS =  (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book avilability'
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return  f'{self.id} ({self.book.title})'

