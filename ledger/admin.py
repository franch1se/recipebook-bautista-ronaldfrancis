from django.contrib import admin
from .models import Recipe, RecipeIngredient

# Register your models here.

class RecipeIngredientInline (admin.TabularInline):
    model = RecipeIngredient
    fields = ['ingredient', 'quantity', 'recipe']

class RecipeAdmin (admin.ModelAdmin):
    model = Recipe

    search_fields = ('name', )
    list_display = ('name', 'id', )
    list_filter = ('name', )

    inlines = [RecipeIngredientInline, ]


admin.site.register(Recipe, RecipeAdmin)