from django.http import JsonResponse # JSON 응답
from food.models import Food_Point
from django.forms.models import model_to_dict


def foodmap_data(request):
    data_2 = Food_Point.objects.all()
    map_list = []
    for d in data_2:
        d = model_to_dict(d) # QuerySet -> Dict
        map_list.append(d)
    return JsonResponse(map_list, safe=False)

