from django.shortcuts import render
from taxi.models import Taxi


def taxi_list(request):
    name = request.GET.get('name')
    plate = request.GET.get('plate')
    d_name = request.GET.get('d_name')
    model = request.GET.get('model')
    stat = request.GET.get('stat')
    if name is not None and plate is not None and d_name is not None and model is not None and stat is not None:
        Meal.objects.create(
            name=name,
            plate=plate,
            d_name=d_name,
            model=model,
            stat=stat,
        )
    taxi = Taxi.objects.all()
    ctx = {'posts': taxi}
    return render(request, 'posts/taxi_list.html', ctx)




