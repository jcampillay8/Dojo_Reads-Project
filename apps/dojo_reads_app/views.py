from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def book(request):
    # if 'id' in request.session:
    #     context = {
    #         'user': User.objects.get(id=request.session['id']),
    #         'postedMessages' : Message.objects.all(),
    #         'postedComments' : Comment.objects.all(),
    #     }
    #     print('user is in session')
    #     return render(request, 'thewall/wall.html', context)
    # return redirect('/')
    return render(request,'books/books_home.html')

def add_book(request):
    context = {
        'all_authors': Author.objects.all()
    }
    if request.method == 'POST':
        existing_author = Author.objects.filter(author=request.POST['author'])
        if len(existing_author) > 0:
            this_author = existing_author[0]
        else:
            this_author = Author.objects.create(author=request.POST['new_author'])
        book = Book.objects.create(title=request.POST['title'], author=this_author)
        Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=book, poster=User.objects.get(id=request.session['user_id']))
        book_id = book.id
        return redirect(f'/books/{book_id}')
    return render(request, 'books/add_book.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')