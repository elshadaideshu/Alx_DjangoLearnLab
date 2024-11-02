from django.urls import path
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("books/", include("book_store.urls")),
    path("admin/", admin.site.urls),
]

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]