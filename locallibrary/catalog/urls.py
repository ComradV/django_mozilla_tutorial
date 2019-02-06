from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.empty_view, name='books'),
    path('authors/', views.empty_view, name='authors'),
    path('book/<id>/', views.empty_view_id, {'id':id}),
    path('author/<id>/', views.empty_view_id, {'id':id}),

    # path('bookdetail/<id>', views.empty_view, name='book-detail')
]
