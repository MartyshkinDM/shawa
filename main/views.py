from django.shortcuts import render
from .models import Shawarmas, Shawarma_points, Workers, Ingredients,Snacks,Drinks,Combos,ShawarmaIngredient
def index(request):
    shawarmas = Shawarmas.objects.all()
    snacks = Snacks.objects.all()
    drinks = Drinks.objects.all()
    combos = Combos.objects.all()
    return render(request, 'main/index.html', {
        'Shawarmas': shawarmas,
        'snacks': snacks,
        'drinks': drinks,
        'combos': combos,
        'ingredients':ShawarmaIngredient
    })
"""
def shawarma_points_list(request):
    points = Shawarma_points.objects.order_by('point_address')
    context = {'points': points}
    return render(request, 'main/shawarma_points_list.html', context)

def workers_list(request):
    workers = Workers.objects.order_by('worker_last_name')
    context = {'workers': workers}
    return render(request, 'main/workers_list.html', context)

def ingredients_list(request):
    ingredients = Ingredients.objects.order_by('ingredient_name')
    context = {'ingredients': ingredients}
    return render(request, 'main/ingredients_list.html', context)
"""