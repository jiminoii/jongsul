from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def food(request):
    return render(request, 'food.html')

def exp(request):
    return render(request, 'exp.html')
    
def festival(request):
    return render(request, 'festival.html')

def stay(request):
    result = requests.get('https://www.tourandong.com/public/sub3/sub2.cshtml')
    result.encoding = 'utf-8'
    result = result.text
    s_table = 0
    e_table = 0
    star = ""
    while True:
        s_table = result.find('<table',e_table)
        s_table = result.find('>',s_table)
        if s_table == -1:
            break;
        e_table = result.find('</table>',s_table)
        star += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
    r_ta = {
        'contact' : star
    }
    return render(request, 'stay.html',r_ta)
