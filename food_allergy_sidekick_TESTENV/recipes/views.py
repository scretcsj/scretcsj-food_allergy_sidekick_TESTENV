from django.shortcuts import get_object_or_404, render, redirect
from .models import Recipe, KeyValueStore
from .forms import RecipeForm, RecipeSearchForm, KeyValueStoreForm, KeyValueStoreSearchForm
from django.conf import settings
from django.http import JsonResponse
import subprocess


# Custom Recipes Model  Views
# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'recipe_list.html', {'recipes': recipes})


# def recipe_detail(request, pk):
#     recipe = get_object_or_404(Recipe, pk=pk)
#     ingredients = recipe.ingredients.split('\n') if recipe.ingredients else []
#     instructions = recipe.instructions.split('\n') if recipe.instructions else []
#     return render(request, 'recipe_detail.html', {
#         'recipe': recipe,
#         'ingredients': ingredients,
#         'instructions': instructions,
#     })


# def search_recipes(request):
#     if request.method == 'GET':
#         form = RecipeSearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(ingredients__icontains=query)
#             return render(request, 'recipe_search.html', {'form': form, 'results': results})
#     else:
#         form = RecipeSearchForm()
#     return render(request, 'recipe_search.html', {'form': form})




# KeyValueStore model views views.
def recipe_list(request):
    recipes = KeyValueStore.objects.all()
    return render(request, 'recipe_list.html', {
        'recipes': recipes,
        })


def recipe_detail(request, pk):
    recipe = get_object_or_404(KeyValueStore, pk=pk)
    ingredients = recipe.ingredients.split('\n') if recipe.ingredients else []
    measurements = recipe.measurements.split('\n') if recipe.measurements else []
    paired_ingredients = zip(ingredients, measurements)  # Pair ingredients and measurements
    instructions = recipe.strinstructions.split('\n') if recipe.strinstructions else []
    image_url = f"{settings.MEDIA_URL}food_pics/{recipe.id}.png"
    return render(request, 'recipe_detail.html', {
        'recipe': recipe,
        'ingredients': ingredients,
        'measurements': measurements,
        'paired_ingredients': paired_ingredients,
        'instructions': instructions,
        'image_url': image_url,
    })


# def recipe_detail(request, pk):
#     recipe = get_object_or_404(KeyValueStore, pk=pk)
#     # Join all stringredient cols into a allIngredients object. Then
#     allIngredients = ingredients.join(
#         recipe.stringredient1,
#         recipe.stringredient2,
#         recipe.stringredient3,
#         recipe.stringredient4,
#         recipe.stringredient5,
#         recipe.stringredient6,
#         recipe.stringredient7,
#         recipe.stringredient8,
#         recipe.stringredient9,
#         recipe.stringredient10,
#         recipe.stringredient11,
#         recipe.stringredient12,
#         recipe.stringredient13,
#         recipe.stringredient14,
#         recipe.stringredient15,
#         recipe.stringredient16,
#         recipe.stringredient17,
#         recipe.stringredient18,
#         recipe.stringredient19,
#         recipe.stringredient20,
#     )
#     allIngredients = recipe.allIngredients.split('\n') if recipe.ingredients else []
#     instructions = recipe.strinstructions.split('\r\n') if recipe.strinstructions else []
#     return render(request, 'recipe_detail.html', {
#         'recipe': recipe,
#         'ingredients': ingredients,
#         'instructions': instructions,
#     })


def search_recipes(request):
    if request.method == 'GET':
        form = KeyValueStoreSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = KeyValueStore.objects.filter(strmeal__icontains=query)
            return render(request, 'recipe_search.html', {'form': form, 'results': results})
    else:
        form = KeyValueStoreSearchForm()
    return render(request, 'recipe_search.html', {'form': form})


def run_script(request):
    if request.method == "POST":
        ingredient = request.POST.get('ingredient')
        script_output = subprocess.check_output(['python', 'scripts/Test.py', ingredient], text=True)
        alternatives = script_output.splitlines()
        return JsonResponse({"script_output": alternatives})
    return JsonResponse({"message": "Invalid request"}, status=400)