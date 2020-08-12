from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from food.models import Food_Point
def index(request):
    return render(request, 'index.html')

def food(request):
    food_point = Food_Point.objects.order_by('-id')
    context = {
        'food_point' : food_point
    }
    return render(request, 'food.html', context)


def exp(request):
    return render(request, 'exp.html')
    
def festival(request):
    return render(request, 'festival.html')

def stay(request):
    return render(request, 'stay.html')
