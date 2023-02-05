from django.shortcuts import render
from .models import Meal

# Create your views here.

def meals(request):
    meals = Meal.objects.all()
    return render(request, 'meals/home.html', {'meals' : meals})