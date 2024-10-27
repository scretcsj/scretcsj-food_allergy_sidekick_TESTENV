from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .models import UserProfile
from recipes.models import Recipe, KeyValueStore
from recipes.forms import RecipeSearchForm, RecipeForm, KeyValueStoreForm, KeyValueStoreSearchForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


# Custom recipe model
# def home(request):
#     form = RecipeSearchForm()
#     recipes = Recipe.objects.all()

#     if request.GET.get('query'):
#             form = RecipeSearchForm(request.GET)
#             if form.is_valid():
#                 query = form.cleaned_data['query']
#                 recipes = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(ingredients__icontains=query)

#     return render(request, 'home.html', {
#         'form': form,
#         'recipes': recipes,
#     })


# KeyValueStore Model
def home(request):
    form = KeyValueStoreSearchForm()
    recipes = KeyValueStore.objects.all()

    if request.GET.get('query'):
            form = KeyValueStoreSearchForm(request.GET)
            if form.is_valid():
                query = form.cleaned_data['query']
                recipes = KeyValueStore.objects.filter(strmeal__icontains=query) | KeyValueStore.objects.filter(stringredient1__icontains=query)

    return render(request, 'home.html', {
        'form': form,
        'recipes': recipes,
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Save allergies to user profile
            user_profile = UserProfile.objects.create(user=user)
            user_profile.allergies = form.cleaned_data['allergies']
            user_profile.save()
            login(request, user)
            messages.success(request, 'You have successfully signed up!')
            return redirect('view_profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Custom Recipe Model
# @login_required
# def view_profile(request):
#     profile, created = UserProfile.objects.get_or_create(user=request.user)
#     allergies = profile.allergies  # Directly access the MSFList
#     recipe_form = RecipeForm()
#     return render(request, 'view_profile.html', {
#         'profile': profile,
#         'allergies': allergies,
#         'recipe_form': recipe_form,
#         })


@login_required
def view_profile(request):
    profile = request.user.userprofile
    form = UserProfileForm(instance=profile)
    recipe_form = KeyValueStoreForm()

    return render(request, 'view_profile.html', {
        'profile': profile,
        'form': form,
        'recipe_form': recipe_form
    })

# Custom Recipe Model form
# @login_required
# def add_recipe(request):
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             recipe = form.save(commit=False)
#             recipe.user = request.user
#             recipe.save()
#             messages.success(request, 'Recipe added successfully!')
#             return redirect('view_profile')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = RecipeForm()
#     return render(request, 'add_recipe.html', {'form': form})


# KeyValueStore Model
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = KeyValueStoreForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('recipe_detail', pk=recipe.pk)  
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = KeyValueStoreForm()
    return render(request, 'add_recipe.html', {'form'})


# @login_required
# adjusting edit profile for extra fields and images
# def edit_profile(request):
#     profile, created = UserProfile.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile has been updated.')
#             return redirect('view_profile')
#     else:
#         form = UserProfileForm(instance=profile)
#     return render(request, 'edit_profile.html', {'form': form})


@login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
            user = profile.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile, initial={
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        })
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('view_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to update the session to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})