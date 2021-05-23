from django.urls import path
from . import views

urlpatterns = [
    path('book', views.book),
    path('books/add', views.add_book),
    path('logout', views.logout),
]