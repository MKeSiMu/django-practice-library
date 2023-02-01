from django.http import Http404
from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, LiteraryFormat


def index(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary_formats": num_literary_formats
    }

    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"
    # queryset = LiteraryFormat.objects.filter(name__endswith="y")


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.all().select_related("format")
    paginate_by = 1


class AuthorListView(generic.ListView):
    model = Author


# def literary_format_list_view(request):
#     literary_format_list = LiteraryFormat.objects.all()
#
#     context = {
#         "literary_format_list": literary_format_list
#     }
#
#     return render(request, "catalog/literary_format_list.html", context=context)

class BookDetailView(generic.DetailView):
    model = Book

# def book_detail_view(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")
#
#     context = {
#         "book": book
#     }
#
#     return render(request, "catalog/book_detail.html", context=context)