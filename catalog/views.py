from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, LiteraryFormat


def index(request):
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()

    num_visit = request.session.get("num_visit", 0)
    request.session["num_visit"] = num_visit + 1

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_literary_formats": num_literary_formats,
        "num_visit": num_visit + 1,
    }

    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(generic.ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"
    # queryset = LiteraryFormat.objects.filter(name__endswith="y")

# def literary_format_list_view(request):
#     literary_format_list = LiteraryFormat.objects.all()
#
#     context = {
#         "literary_format_list": literary_format_list
#     }
#
#     return render(request, "catalog/literary_format_list.html", context=context)


class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.all().select_related("format")
    paginate_by = 1


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


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author
    queryset = Author.objects.all().prefetch_related("books__format")

def test_session_view(request):
    return HttpResponse(
        "<h1>Test Session</h1>"
        f"<h4>Session data: {request.session['book']}</h4>"
    )
