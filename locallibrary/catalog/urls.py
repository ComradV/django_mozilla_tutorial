from django.urls import path
from . import views

urlpatterns = [
    path('', views.empty_view),
    # path('bookdetail/<id>', views.empty_view, name='book-detail')
]
