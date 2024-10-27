### Coding Challenges

> I tried displaying the allergies within the admin console and received an MSFList error. Feedback: The error you're seeing is because MultiSelectField returns a list-like object (MSFList) which doesn't have an .all() method. 
Instead, you should iterate directly over the allergies attribute without calling .all().

> Cannot add new recipes as the current model is not auto generating a unique ID

### Insights

> Combined all stringredient cols using the following:

```python
from recipes.models import KeyValueStore

# Assuming you have up to 20 ingredients and measurements
for recipe in KeyValueStore.objects.all():
    combined_ingredients = []
    for i in range(1, 21):
        ingredient = getattr(recipe, f'stringredient{i}')
        measure = getattr(recipe, f'strmeasure{i}')
        if ingredient and measure:
            combined_ingredients.append(f'{measure} {ingredient}')
        elif ingredient:
            combined_ingredients.append(ingredient)
    recipe.ingredients = '\n'.join(combined_ingredients)
    recipe.save()
```

<details>

<summary>Project Changes</summary>

> 10/27/24
- [x] Combined measures and ingredients into new model fields for easier integration into html view

> 10/26/24

- [x] Moved sample recipes over to this project for additional testing.
- [x] Search feature built into sample .db as well.
- [x] Click to see alternative milestone working
- [x] Images are now explicited called based on recipe unique ID

> 10/25/24

- [x] Sample Recipes added at admin console
- [x] Search functionality. User can search by title or ingredient.
- [x] Users can add a recipe from their profile. Some logic built into view to break steps and ingredients into separate line based on '\n' characters

> 10/24/24

- [x] Additional profile fields can be updated. First and Last name
- [x] Users can add profile images

> 10/22/24

- [x] Moved User creation and allergy customization to this testenv

</details>

### Major Features

- [x] User Profile
- [x] User Profile (custom detials)
- [x] Search recipes in .db
- [x] Alternative suggestions
- [ ] User can add recipes to .db
 