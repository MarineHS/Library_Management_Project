from django.urls import path
from . import views

app_name = 'Catalog'

urlpatterns = [
    path('', views.catalog_home, name='catalog_home'),
    path('search/', views.book_search, name='book_search'), # URL search
    path('book/<str:isbn>/', views.book_details, name='book_details'), # book details
]