from django.urls import path

from .views import RecipeListView, RecipeLoggedInView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>/ingredients', RecipeLoggedInView.as_view(), name='recipes')
]

app_name = "ledger"