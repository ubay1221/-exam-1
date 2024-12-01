from django.shortcuts import render
from meals.models import Meal


def meal_list(request):
    name = request.GET.get('name')
    igredients = request.GET.get('igredients')
    price = request.GET.get('price')
    type = request.GET.get('type')
    cuisine = request.GET.get('cuisine')
    if name is not None and igredients is not None and price is not None and type is not None and cuisine is not None:
        Meal.objects.create(
            name=name,
            igredients=igredients,
            price=price,
            type=type,
            cuisine=cuisine,
        )
    meal = Meal.objects.all()
    ctx = {'posts': meal}
    return render(request, 'posts/meal_list.html', ctx)




