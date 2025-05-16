from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_food, name='add_food'),
    path('delete/<int:id>/', delete_food, name='delete_food'),
    path('reset/', reset_day, name='reset_day'),
]
