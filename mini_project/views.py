from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from exp.models import Inpo

def index(request):
    return render(request, 'index.html')

def food(request):
    return render(request, 'food.html')

def exp(request):
    info_list = Inpo.objects.order_by('-id')
    context = {
    'info_list' : info_list
    }
    return render(request, 'exp.html', context)
    
def festival(request):
    return render(request, 'festival.html')

def stay(request):
    return render(request, 'stay.html')


