from django.urls import path
from .views import find_shortest_path, grid_view

urlpatterns = [
    path('', grid_view, name='grid_view'),  # Main page to view grid
    path('find-path/', find_shortest_path, name='find_path'),
]