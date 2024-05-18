from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("<int:id>", views.book_details, name="book-details")
]