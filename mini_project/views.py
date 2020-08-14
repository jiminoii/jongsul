from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from food.models import Food_Inpo
from exp.models import Inpo
import requests
from bs4 import BeautifulSoup as bs
from user.models import User
from user.models import Board
def index(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        # 회원정보 저장
        id1 = request.POST.get('id1')
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        users = User(id1=id1, name=name, pwd=pwd)
        users.save()
        return HttpResponseRedirect('/')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
    # 회원정보 조회
        id1 = request.POST.get('id1')
        pwd = request.POST.get('pwd')
        try:
        # select * from user where email=? and pwd=?
            user = User.objects.get(id1=id1, pwd=pwd)
            request.session['id1'] = id1
            
            return render(request, 'signin_success.html')
        except:
            return render(request, 'signin_fail.html')
    return render(request, 'signin.html')


def signout(request):
    del request.session['id1'] # 개별 삭제
    request.session.flush() # 전체 삭제
    return HttpResponseRedirect('/')

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
    stra ="<table class='table table-hover'><thead><tr><th style='text-align: center;'>상호명</th><th style='text-align: center;'>주소</th><th style='text-align: center;'>전화번호</th></tr></thead>"
    i=0
    parse = bs(res.text, 'html.parser')
    a_list = parse.select('#contentDiv a p')
    a_list2 = parse.select('.tour_course_thum strong')
    loc_list=[]
    tel=""
    for a in a_list:
        obj={}
        stra+="<tr>"
        stra+="<td>"+ a_list2[i].text + "</td>"
        i+=1
        if a.text.find('전화') != -1:
            stra += '<td>'+(a.text)[5:a.text.find('전화')]+'</td>'
            juso=(a.text)[5:a.text.find('전화')]
            stra += '<td>'+(a.text)[a.text.find('전화')+5:-6]+'</td>'
            tel=(a.text)[a.text.find('전화')+5:-7]
        else:
            stra += '<td>'+(a.text)[5:-6]+'</td><td></td>'
            juso=(a.text)[5:-6]
        stra+="</tr>"
        urla=" https://maps.googleapis.com/maps/api/geocode/json?address="+juso+"&key=AIzaSyBiulBepetV6p2prBzpL-K7ss2-b_xP5NU"
        res = requests.get(urla)
        parse=res.json()
        ress=parse['results']
        geo=ress[0].get('geometry')
        loc=geo['location']
        lat=loc.get('lat')
        lng=loc.get('lng')
        obj['lat'] = lat
        obj['lng'] = lng
        obj['tel'] = tel
        loc_list.append(obj)

    stra+="</table>"
    

    address2 = 'https://www.tourandong.com/public/sub2/sub5.cshtml'
    res = requests.get(address2)
    res.encoding = None
    strb ="<table class='table table-hover'><thead><tr><th style='text-align: center;'>상호명</th><th style='text-align: center;'>주소</th><th style='text-align: center;'>전화번호</th></tr></thead>"
    
    i=0
    parse = bs(res.text, 'html.parser')
    a_list = parse.select('#contentDiv a p')
    a_list2 = parse.select('.tour_course_thum strong')
    loc_list1=[]
    for a in a_list:
        obj={}
        strb+="<tr>"
        strb+="<td>"+ a_list2[i].text + "</td>"
        i+=1
        if a.text.find('전화') != -1:
            strb += '<td>'+(a.text)[5:a.text.find('전화')]+'</td>'
            juso=(a.text)[5:a.text.find('전화')]
            strb += '<td>'+(a.text)[a.text.find('전화')+5:-6]+'</td>'
            tel=(a.text)[a.text.find('전화')+5:-7]
        else:
            strb += '<td>'+(a.text)[5:-6]+'</td><td></td>'
            juso=(a.text)[5:-6]
        strb+="</tr>"
        urla=" https://maps.googleapis.com/maps/api/geocode/json?address="+juso+"&key=AIzaSyBiulBepetV6p2prBzpL-K7ss2-b_xP5NU"
        res = requests.get(urla)
        parse=res.json()
        ress=parse['results']
        geo=ress[0].get('geometry')
        loc=geo['location']
        lat=loc.get('lat')
        lng=loc.get('lng')
        obj['lat'] = lat
        obj['lng'] = lng
        obj['tel'] = tel
        loc_list1.append(obj)
    strb+="</table>"

    address3 = 'https://www.tourandong.com/public/sub2/sub6.cshtml'
    res = requests.get(address3)
    res.encoding = None
    strc ="<table class='table table-hover'><thead><tr><th style='text-align: center;'>상호명</th><th style='text-align: center;'>개화시기</th><th style='text-align: center;'>주변관광지</th></tr></thead>"
    i=0
    parse = bs(res.text, 'html.parser')
    a_list = parse.select('.flower_spot ul li')
    a_list2 = parse.select('.flower_spot dt')
    for a in a_list2:
        obj={}
        strc+="<tr>"
        strc+="<td>"+ a.text + "</td>"
        strc += '<td>'+(a_list[i].text)[6:]+'</td>'
        strc += '<td>'+(a_list[i+1].text)[7:]+'</td>'
        i+=2
        strc+="</tr>"
    strc+="</table>"



    aa = {
        'gg' : info_list,
        'contact' : stra,
        'contact2' : strb,
        'contact3' : strc,
        'loc_contact':loc_list,
        'loc_contact1':loc_list1,
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
    star = ''
    parse = bs(result,'html.parser')
    latlngs = parse.select('tbody tr')
    tds = parse.select('tbody td')
    i = 0
    data = []
    for latlan in latlngs:
        obj = {}
        obj['latlan'] = latlan['data-map']
        if tds[i*4].text.find('\n') == -1:
            obj['place'] = tds[i*4].text
        else:
            obj['place'] = tds[i*4].text[:tds[i*4].text.find('\n')-1]+tds[i*4].text[tds[i*4].text.find('\n')+1:]
        if tds[i*4+2].text.find('\n') == -1:
            obj['tel'] = tds[i*4+2].text
        else:
            obj['tel'] = tds[i*4+2].text[:tds[i*4+2].text.find('\n')-1]
        i+=1
        data.append(obj)
    while True:
        s_table = result.find('<table',e_table)
        s_table = result.find('>',s_table)
        if s_table == -1:
            break
        e_table = result.find('</table>',s_table)
        star += '<table class="table table-hover"'+result[s_table:e_table+8]
    result = requests.get('https://www.tourandong.com/public/sub3/sub2_2.cshtml')
    result.encoding = 'utf-8'
    result = result.text
    s_table = 0
    e_table = 0
    star1 = ""
    parse = bs(result,'html.parser')
    latlngs = parse.select('tbody tr')
    tds = parse.select('tbody td')
    i = 0
    data1 = []
    for latlan in latlngs:
        obj = {}
        obj['latlan'] = latlan['data-map']
        if tds[i*4].text.find('\n') == -1:
            obj['place'] = tds[i*4].text
        else:
            obj['place'] = tds[i*4].text[:tds[i*4].text.find('\n')-1]+tds[i*4].text[tds[i*4].text.find('\n')+1:]
        if tds[i*4+2].text.find('\n') == -1:
            obj['tel'] = tds[i*4+2].text
        else:
            obj['tel'] = tds[i*4+2].text[:tds[i*4+2].text.find('\n')-1]
        i+=1
        data1.append(obj)
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
    parse = bs(result,'html.parser')
    latlngs = parse.select('tbody tr')
    tds = parse.select('tbody td')
    i = 0
    data2 = []
    for latlan in latlngs:
        obj = {}
        obj['latlan'] = latlan['data-map']
        if tds[i*5].text.find('\n') == -1:
            obj['place'] = tds[i*5].text
        else:
            obj['place'] = tds[i*5].text[:tds[i*5].text.find('\n')-1]+tds[i*5].text[tds[i*5].text.find('\n')+1:]
        if tds[i*5+2].text.find('\n') == -1:
            obj['tel'] = tds[i*5+2].text
        else:
            obj['tel'] = tds[i*5+2].text[:tds[i*5+2].text.find('\n')-1]
        i+=1
        data2.append(obj)
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
    parse = bs(result,'html.parser')
    latlngs = parse.select('tbody tr')
    tds = parse.select('tbody td')
    i = 0
    data3 = []
    for latlan in latlngs:
        obj = {}
        obj['latlan'] = latlan['data-map']
        if tds[i*5].text.find('\n') == -1:
            obj['place'] = tds[i*5].text
        else:
            obj['place'] = tds[i*5].text[:tds[i*5].text.find('\n')-1]+tds[i*5].text[tds[i*5].text.find('\n')+1:]
        if tds[i*5+2].text.find('\n') == -1:
            obj['tel'] = tds[i*5+2].text
        else:
            obj['tel'] = tds[i*5+2].text[:tds[i*5+2].text.find('\n')-1]
        i+=1
        data3.append(obj)
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
    parse = bs(result,'html.parser')
    latlngs = parse.select('tbody tr')
    tds = parse.select('tbody td')
    i = 0
    for latlan in latlngs:
        obj = {}
        obj['latlan'] = latlan['data-map']
        if tds[i*4].text.find('\n') == -1:
            obj['place'] = tds[i*4].text
        else:
            obj['place'] = tds[i*4].text[:tds[i*4].text.find('\n')-1]+tds[i*4].text[tds[i*4].text.find('\n')+1:]
        if tds[i*4+2].text.find('\n') == -1:
            obj['tel'] = tds[i*4+2].text
        else:
            obj['tel'] = tds[i*4+2].text[:tds[i*4+2].text.find('\n')-1]
        i+=1
        data.append(obj)
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
    parse = bs(result,'html.parser')
    latlngs = parse.select('tbody tr')
    tds = parse.select('tbody td')
    i = 0
    for latlan in latlngs:
        obj = {}
        obj['latlan'] = latlan['data-map']
        if tds[i*4].text.find('\n') == -1:
            obj['place'] = tds[i*4].text
        else:
            obj['place'] = tds[i*4].text[:tds[i*4].text.find('\n')-1]+tds[i*4].text[tds[i*4].text.find('\n')+1:]
        if tds[i*4+2].text.find('\n') == -1:
            obj['tel'] = tds[i*4+2].text
        else:
            obj['tel'] = tds[i*4+2].text[:tds[i*4+2].text.find('\n')-1]
        i+=1
        data1.append(obj)
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
        'data' : data,
        'data1' : data1,
        'data2' : data2,
        'data3' : data3,
    }
    return render(request, 'stay.html',r_ta)

def festival2(request):
    return render(request, 'festival2.html')

def festival3(request):
    return render(request, 'festival3.html')

def festival4(request):
    return render(request, 'festival4.html')

def community(request):
    return render(request, 'community.html')

def write(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            id1 = request.session['id1']
            # # select * from user where email = ?
            user = User.objects.get(id1=id1)
            # insert into article (title, content, user_id) values (?, ?, ?)
            board = Board(title=title, content=content, id1=user)
            board.save()
            return render(request, 'commu_success.html')
        except:
            return render(request, 'commu_fail.html')

    return render(request, 'commu_write.html')

def list(request):

    commu_list = Board.objects.order_by('-id')
    context = {
        'commu_list' : commu_list
    }
    return render(request, 'commu_list.html', context)

def detail(request, id):
    # select * from article where id = ?
    board = Board.objects.get(id=id)
    context = {
        'board' : board
    }

    return render(request, 'detail.html', context)

def update(request, id):
    # select * from article where id = ?
    board = Board.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # update article set title = ?, content = ? where id = ?
            board.title = title
            board.content = content
            board.save()
            return render(request, 'update_success.html')
        except:
            return render(request, 'update_fail.html')
    context = {
    'board' : board
    }
    return render(request, 'update.html', context)
