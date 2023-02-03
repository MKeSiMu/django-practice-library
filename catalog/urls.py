from django.urls import path

from catalog.views import (
    index,
    LiteraryFormatListView,
    LiteraryFormatCreateView,
    LiteraryFormatUpdateView,
    LiteraryFormatDeleteView,
    BookListView,
    AuthorListView,
    BookDetailView,
    AuthorDetailView,
    test_session_view,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "literary-format/",
        LiteraryFormatListView.as_view(),
        name="literary-format-list"
    ),
    path(
        "literary-format/create/",
        LiteraryFormatCreateView.as_view(),
        name="literary-format-create"
    ),
    path(
        "literary-format/<int:pk>/update/",
        LiteraryFormatUpdateView.as_view(),
        name="literary-format-update"
    ),
    path(
        "literary-format/<int:pk>/delete/",
        LiteraryFormatDeleteView.as_view(),
        name="literary-format-delete"
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
