from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from food.models import Food_Inpo
from exp.models import Inpo
import requests
from bs4 import BeautifulSoup as bs

def index(request):
    return render(request, 'index.html')

def food(request):
    # food_point = Food_Inpo.objects.order_by('id')
    # context = {
    # 'food_point' : food_point
    # }
    # return render(request, 'food.html', context)
    result = requests.get('https://www.tourandong.com/public/sub3/sub1.cshtml')
    result.encoding = 'utf-8'
    result = result.text
    s_table = 0
    e_table = 0
    star = ["","","","","","","","","","","","","","",]
    i=0
    while True:
        s_table = result.find('<table',e_table)
        s_table = result.find('>',s_table)        
        if s_table == -1:
            break
        e_table = result.find('</table>',s_table)
        star[i] += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
        i+=1
    r_ta = {
        'contact' : star[0],
        'contact1' : star[1],
        'contact2' : star[2],
        'contact3' : star[3],
        'contact4' : star[4],
        'contact5' : star[5],
        'contact6' : star[6],
    }
    return render(request, 'food.html',r_ta)

    

def exp(request):
    info_list = Inpo.objects.order_by('id')
    address = 'https://www.tourandong.com/public/sub2/sub4.cshtml'
    res = requests.get(address)
    res.encoding = None
    stra =""
    strb =""
    parse = bs(res.text, 'html.parser')
    a_list = parse.select('#contentDiv a p')
    for a in a_list:
        if a.text.find('전화') != -1:
            stra += (a.text)[5:a.text.find('전화')]+'<br/>'
            strb += (a.text)[a.text.find('전화')+5:]+'<br/>'
        else:
            stra += (a.text)[5:-6]+'<br/>'
    aa = {
        'contact' : stra,
        'contact1' : strb,
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
            break
        e_table = result.find('</table>',s_table)
        star += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
    result = requests.get('https://www.tourandong.com/public/sub3/sub2_2.cshtml')
    result.encoding = 'utf-8'
    result = result.text
    s_table = 0
    e_table = 0
    star1 = ""
    while True:
        s_table = result.find('<table',e_table)
        s_table = result.find('>',s_table)
        if s_table == -1:
            break
        e_table = result.find('</table>',s_table)
        star1 += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
    result = requests.get('https://www.tourandong.com/public/sub3/sub2_3.cshtml')
    result.encoding = 'utf-8'
    result = result.text
    s_table = 0
    e_table = 0
    star2 = ""
    while True:
        s_table = result.find('<table',e_table)
        s_table = result.find('>',s_table)
        if s_table == -1:
            break
        e_table = result.find('</table>',s_table)
        star2 += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
    result = requests.get('https://www.tourandong.com/public/sub3/sub2_4.cshtml')
    result.encoding = 'utf-8'
    result = result.text
    s_table = 0
    e_table = 0
    star3 = ""
    while True:
        s_table = result.find('<table',e_table)
        s_table = result.find('>',s_table)
        if s_table == -1:
            break
        e_table = result.find('</table>',s_table)
        star3 += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
    result = requests.get('https://www.tourandong.com/public/sub3/sub2_1.cshtml')
    result.encoding = 'utf-8'
    result = result.text
    s_table = 0
    e_table = 0
    star4 = ""
    while True:
        s_table = result.find('<table',e_table)
        s_table = result.find('>',s_table)
        if s_table == -1:
            break
        e_table = result.find('</table>',s_table)
        star4 += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
    result = requests.get('https://www.tourandong.com/public/sub3/sub2_2_1.cshtml')
    result.encoding = 'utf-8'
    result = result.text
    s_table = 0
    e_table = 0
    star5 = ""
    while True:
        s_table = result.find('<table',e_table)
        s_table = result.find('>',s_table)
        if s_table == -1:
            break
        e_table = result.find('</table>',s_table)
        star5 += '<div class="jumbotron"><table class="table table-hover"'+result[s_table:e_table+8]+'</div>'
    r_ta = {
        'contact' : star,
        'contact1' : star1,
        'contact2' : star2,
        'contact3' : star3,
        'contact4' : star4,
        'contact5' : star5,
    }
    return render(request, 'stay.html',r_ta)

def community(request):
    return render(request, 'community.html')

def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
        email = request.session['email']
        # select * from user where email = ?
        user = User.objects.get(email=email)
        # insert into article (title, content, user_id) values (?, ?, ?)
        article = Article(title=title, content=content, user=user)
        article.save()
        return render(request, 'commu_success'.html')
    except:
        return render(request, 'commu_fail.html')

    return render(request, 'commu_write.html')

def list(request):

    board_list = Board.objects.order_by('id')
    context = {
        'board_list' : board_list
    }
    return render(request, 'commu_list.html', context)
