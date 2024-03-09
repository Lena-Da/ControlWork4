from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from .models import Recipe
from .forms import RecipeForm


def index(request):
    recipes = Recipe.objects.all().order_by('?')[:5]

    context = {
        'recipes': recipes
    }

    return render(request, 'main/index.html', context)


def recipe(request, recipe_id):
    recipe_obj = Recipe.objects.get(id=recipe_id)
    steps_without_empty_lines = [step.strip() for step in recipe_obj.steps.split('\r') if step.strip()]
    recipe_obj.steps = mark_safe('<p>' + '</p><p>'.join(steps_without_empty_lines) + '</p>')

    return render(request, 'main/recipe.html', {'recipe': recipe_obj})


def add(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        print(form.errors, form.is_valid(), request.FILES.get('image'))
        if form.is_valid():
            new_recipe = form.save(commit=False)
            form.save()

            return redirect('recipe', recipe_id=new_recipe.id)

    return render(request, 'main/add.html', {'form': form, 'success': False})


def change(request, recipe_id):
    form = RecipeForm(instance=Recipe.objects.get(id=recipe_id))

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=Recipe.objects.get(id=recipe_id))
        if form.is_valid():
            form.save()

            return redirect('recipe', recipe_id=recipe_id)

    return render(request, 'main/change.html', {'form': form, 'success': False})
