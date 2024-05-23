from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),  
    path('books/', include('books.urls')),
    path('transactions/', include('transactions.urls')),
    path('', views.home, name='home'),  
    path('category/<slug:category_slug>/', views.home, name='category_wise_view'),
    path('books/details/<int:pk>/', views.DetailBookView.as_view(), name='Book_detail'),
    path('borrow-book/<int:book_id>/', views.Borrow_Book, name='borrow_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
