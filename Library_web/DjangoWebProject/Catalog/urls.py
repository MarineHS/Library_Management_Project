from django.urls import path
from . import views

app_name = 'Catalog'

urlpatterns = [
    path('search/', views.book_search, name='book_search'),
    path('book/<str:isbn>/', views.book_details, name='book_details'),
]