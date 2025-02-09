from django.shortcuts import render
import random

# def home(request):
#     return render(request, "home.html")

def home(request):
    grid_size = 20
    grid_data = [[0] * grid_size for _ in range(grid_size)]  # Initialize grid with zeros
    context = {'grid': grid_data, 'grid_size': grid_size}
    return render(request, 'home.html', context)