from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def food(request):
    return render(request, 'food.html')

def exp(request):
    return render(request, 'exp.html')
    
def festival(request):
    return render(request, 'festival.html')

def stay(request):
    return render(request, 'stay.html')


