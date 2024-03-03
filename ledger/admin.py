from django.contrib import admin
from .models import *

# Register your models here.

class RecipeIngredientInline (admin.TabularInline):
    model = RecipeIngredient
    fields = ['ingredient', 'quantity', 'recipe']

class RecipeAdmin (admin.ModelAdmin):
    model = Recipe

    search_fields = ('name', 'id')
    list_display = ('name', 'id', )

    inlines = [RecipeIngredientInline, ]

class IngredientAdmin (admin.ModelAdmin):
    model = Ingredient

    search_fields = ('name', )
    list_display = ('name', )

    inlines = [RecipeIngredientInline, ]


class RecipeIngredientAdmin (admin.ModelAdmin):
    model = RecipeIngredient

    search_fields = ('recipe', 'ingredient' , 'quantity')
    list_display = ('ingredient' , 'quantity', 'recipe')
    list_filter = ('recipe', 'ingredient')

    fieldsets = [
        ('Details', {
            'fields': [
            'recipe', 'ingredient', 'quantity', 
            ]
            }),
    ]

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)