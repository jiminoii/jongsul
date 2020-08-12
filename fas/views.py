from django.http import JsonResponse # JSON 응답
from fas.models import Point
from django.forms.models import model_to_dict
def map_data(request):
    data = Point.objects.all()
    map_list = []
    for d in data:
        d = model_to_dict(d) # QuerySet -> Dict
        map_list.append(d)
        # dict가 아닌 자료는 항상 safe=False 옵션 사용
    return JsonResponse(map_list, safe=False)
