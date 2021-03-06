from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def insert(request):
    for i in range(1, 123): # 게시물 122 개 입력
        data = Data(text='Data-%s' % i, cre_date=timezone.now())
        data.save()
    return HttpResponse('insert 122')

def list(request):
    #요청받은 모든 데이터는 문자열
    page = request.GET.get('page')

    datas = Data.objects.order_by('-id')
    p = Paginator(datas, 10)
    info = p.page(page)
    context = {
        'info' : info
    }
    return render(request, 'list.html', context)

def pagination(request):
    result = ''
    datas = Data.objects.order_by('-id')
    p = Paginator(datas, 10)
    result += '전체 데이터 수 - %s<br>' % p.count
    result += '전체 페이지 수 - %s<hr>' % p.num_pages

    p = p.page(1)
    list = str(p.object_list).replace('<', '&lt;').replace('>', '&gt;')
    result += '1 페이지 데이터 - %s<hr>' % list

    result += '현재 페이지 데이터 시작번호 - %s<br>' % p.start_index()
    result += '현재 페이지 데이터 종료번호 - %s<hr>' % p.end_index()

    result += '이전 페이지 존재유무 - %s<br>' % p.has_previous()
    if p.has_previous():
        result += '이전 페이지 번호 - %s<br>' % p.previous_page_number()
    result += '다음 페이지 존재유무 - %s<br>' % p.has_next()
    if p.has_next():
        result += '다음 페이지 번호 - %s<br>' % p.next_page_number()
    return HttpResponse(result)