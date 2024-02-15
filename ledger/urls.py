from django.urls import path

from .views import recipe_list, list_1, list_2

urlpatterns = [
    path('recipes/list', recipe_list, name='list'),
    path('recipe/1', list_1, name='1'),
    path('recipe/2', list_2, name='2'),
]

app_name = "ledger"