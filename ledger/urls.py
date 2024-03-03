from django.urls import path

from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/list', recipe_list, name='list'),
    path('recipe/<int:id>/ingredients', recipe_detail, name='recipe-detail')
]

app_name = "ledger"