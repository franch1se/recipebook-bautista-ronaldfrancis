from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, RecipeIngredient

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
