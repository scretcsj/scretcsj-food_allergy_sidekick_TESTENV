from django.urls import path
from .views import recipe_list, recipe_detail, search_recipes, run_script


urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('<int:pk>/', recipe_detail, name='recipe_detail'),
    path('search/', search_recipes, name='search_recipes'),
    path('scripts/', run_script, name='run_script'),
]
