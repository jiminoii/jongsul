from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def food(request):
    return render(request, 'food.html')
    
def festival(request):
    return render(request, 'festival.html')

def stay(request):
    return render(request, 'stay.html')

def travel(request):
    return render(request, 'travel.html')