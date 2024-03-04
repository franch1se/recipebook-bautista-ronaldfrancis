from django.db import models
from django.urls import reverse

# Create your models here.


class Recipe (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url (self):
        return reverse ('recipes', args=str[self.name])

class Ingredient (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url (self):
        return reverse ('ingredient', args=str[self.name])
    
class RecipeIngredient (models.Model):
    quantity = models.CharField(max_length=100)

    recipe = models.ForeignKey (
        Recipe, 
        on_delete=models.CASCADE, 
        related_name = 'ingredients'
    )
    ingredient = models.ForeignKey (
        Ingredient, null=True, 
        on_delete=models.CASCADE, 
        related_name = 'recipes'
    )