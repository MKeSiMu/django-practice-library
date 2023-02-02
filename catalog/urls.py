from django.urls import path

from catalog.views import index, LiteraryFormatListView, BookListView, AuthorListView, BookDetailView, AuthorDetailView, test_session_view

urlpatterns = [
    path("", index, name="index"),
    path(
        "literary_format/",
        LiteraryFormatListView.as_view(),
        name="literary-format-list"
    ),
    path(
        "books/",
        BookListView.as_view(),
        name="book-list"
    ),
    path(
        "books/<int:pk>/",
        BookDetailView.as_view(),
        name="book-detail"
    ),
    path(
        "authors/",
        AuthorListView.as_view(),
        name="author-list"
    ),
    path(
        "authors/<int:pk>/",
        AuthorDetailView.as_view(),
        name="author-detail"
    ),
    path(
        "test-session/",
        test_session_view,
        name="test-session"
    )
]

app_name = "catalog"
