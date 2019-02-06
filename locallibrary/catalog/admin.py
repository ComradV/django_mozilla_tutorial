from django.contrib import admin

from catalog.models import Author, Genre, Language, Book, BookInstance

admin.site.register(Genre)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    model=Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    fk_name = 'book'
    max_num = 4
    extra = 0
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Avilability', {
            'fields': [('status')] 
        })
    )    

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


def make_avilable(modeladmin, request, queryset):
    queryset.update(status='a', due_back=None)

make_avilable.short_description = 'Make selected book instances avilable'

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    actions = [make_avilable]

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Avilability', {
            'fields': [('status', 'due_back')] 
        })
    )
