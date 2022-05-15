from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render

from .models import Book, Comment
from .forms import CommentForm

class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


def book_detail_view(request, pk):
    global comment_form
    book = get_object_or_404(Book, pk=pk)
    #get book comments
    book_comments = book.comments.all()

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()

    context = {
        'book' : book,
        'comments' : book_comments,
        'comment_form' : comment_form,
    }
    return render(request, 'books/book_detail.html', context)

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price', 'book_cover']


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'author', 'description', 'price', 'book_cover']


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

