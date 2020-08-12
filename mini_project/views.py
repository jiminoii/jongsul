from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from exp.models import Inpo
import requests
from bs4 import BeautifulSoup as bs

def index(request):
    return render(request, 'index.html')

def food(request):
    return render(request, 'food.html')

def exp(request):
    info_list = Inpo.objects.order_by('id')
    address = 'https://www.tourandong.com/public/sub2/sub4.cshtml'
    res = requests.get(address)
    res.encoding = None
    stra =""
    parse = bs(res.text, 'html.parser')
    a_list = parse.select('#contentDiv a p')
    for a in a_list:
        stra += (a.text)[:-6]+'<br/>'
    aa = {
        'contact' : stra,
        'gg' : info_list,
    }
    return render(request, 'exp.html', aa)
    

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
        star += '<table class="table table-hover"'+result[s_table:e_table+8]
    r_ta = {
        'contact' : star
    }
    return render(request, 'stay.html',r_ta)
