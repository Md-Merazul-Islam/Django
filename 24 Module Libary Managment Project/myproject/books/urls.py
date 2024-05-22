from django.urls import path
from . import views

urlpatterns = [
    path('book-list/', views.BookListView.as_view(), name='book_list'),
    path('',views.Book_list_by_Category,name='book_list'),
    path('category/<slug:category_slug>/',views.Book_list_by_Category,name='category_wise_view'),

]