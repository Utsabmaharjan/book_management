from django.urls import path
from book.views import Create_form, List
urlpatterns = [
    path('create', Create_form, name= "create_book"),
    path('', List.as_view(), name= "book_list")
]
