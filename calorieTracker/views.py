from django.shortcuts import render, redirect
from .models import FoodItem
from django.utils import timezone

def index(request):
    today = timezone.now().date()
    foods = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in foods)
    return render(request, 'index.html', {'foods': foods, 'total_calories': total_calories})

def add_food(request):
    if request.method == "POST":
        name = request.POST.get('name')
        calories = int(request.POST.get('calories'))
        FoodItem.objects.create(name=name, calories=calories)
    return redirect('index')

def delete_food(request, id):
    FoodItem.objects.get(id=id).delete()
    return redirect('index')

def reset_day(request):
    today = timezone.now().date()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('index')