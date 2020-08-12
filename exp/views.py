from django.http import JsonResponse # JSON 응답
from exp.models import Point
from django.forms.models import model_to_dict


def expmap_data(request):

    data = Point.objects.all()
    map_list = []
    for d in data:
        d = model_to_dict(d) # QuerySet -> Dict
        map_list.append(d)
    return JsonResponse(map_list, safe=False)

