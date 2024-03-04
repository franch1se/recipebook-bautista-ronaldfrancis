from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, Ingredient, RecipeIngredient

# Create your views here.

def recipe_list (request):
    ctx = {
        "recipes" : Recipe.objects.all()
        }
    return render(request, 'recipebook.html', ctx)

def recipe_detail (request, id): 
    ctx = {
        "name": Recipe.objects.get(id=id).name, 
        "ingredients": RecipeIngredient.objects.filter (recipe__id=id)
        }
    return render(request, 'recipelist.html', ctx)
