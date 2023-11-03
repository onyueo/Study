from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
import base64
import io


# keyword
# GET: 키워드 입력 폼 + 현재 Keyword Table에 저장된 데이터 출력
# POST: 키워드 입력 + 저장 + keyword.html로 리디렉트
def keyword(request):
    
    # keywords : Keyword Table에 저장된 전체 데이터
    keywords = Keyword.objects.all()
    
    # method가 POST일 때
    if request.method == 'POST':
        # form : KeywordForm에 입력된 값
        form = KeywordForm(request.POST)
        
        # keywordForm에 올바른 값이 입력된 경우 저장 + keyword.html로 리디렉트
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')
    
    # method가 GET일 때
    else:
        # 키워드 입력 폼 생성
        form = KeywordForm()
        
    # method가 GET인 경우 + KeywordForm에 제대로 된 값이 저장되지 않은 경우
    context = {
        'form':form,
        'keywords':keywords,
    }
    # keyword.html을 렌더링
    return render(request, 'trends/keyword.html', context)
    

# keyword_detail
# POST로만 입력됨
# 삭제버튼을 누른 키워드를 Keyword table에서 조회 + 제거
def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    
    # 밑의 두 줄은 필요 X
    # trend table에서 조회 + 제거
    trend = Trend.objects.get(name=keyword.name)
    trend.delete()
    return redirect('trends:keyword')
    

# crawling
# GET으로만 입력됨
# Keyword 테이블에서 키워드 전체 조회
# 키워드를 검색 + Trend table에 저장
# 키워드가 이미 Trend table에 있는 경우에는 Trend table에 저장된 데이터를 수정
def crawling(request):
    # Keyword 테이블에서 키워드 전체 조회
    keywords = Keyword.objects.all()
    
    # 각 키워드를 검색 + Trend table에 저장
    for keyword in keywords:
        url = f'https://www.google.com/search?q={keyword.name}'
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # soup.select_one('div#result-stats').text 결과 => 검색결과 약 803,000,000개 (0.28초) 
        # split() -> list로 변경 ['검색결과','약','803,000,000개','(0.28초)']
        # [2][0:-1] -> 3번째 요소를 슬라이싱 '803,000,000'
        # replace(',','') -> ,제거 '803000000'
        # int() -> integer 타입 변경 803000000
        result_stats = int(soup.select_one('div#result-stats').text.split()[2][0:-1].replace(',',''))
        
        # temp : Trend 테이블 내 키워드 존재 여부 확인 
        temp = Trend.objects.filter(name=keyword.name).count()
        if temp:
            # Trend 테이블 내에 키워드 존재 -> result만 수정
            # trend : 이미 존재하는 Trend model 인스턴스 검색
            trend = Trend.objects.filter(name=keyword.name)
            trend.result = result_stats
        else:
            # Trend 테이블 내에 키워드 존재하지 않음 -> 데이터 생성
            # trend : 새로 Trend model 인스턴스 생성
            trend = Trend(name=keyword.name, result = result_stats, search_period = 'all')
        # 데이터를 테이블 내에 저장
        trend.save()
        
    # trends: Trend 테이블 내 모든 데이터 
    trends = Trend.objects.all()
    
    context = {
        'trends':trends,
    }
    return render(request, 'trends/crawling.html', context)
    

# crawling_histogram
# 전체 기간 검색 결과 (Trend 테이블의 search_period = 'all'인 데이터)   
def crawling_histogram(request):
    # Trend 테이블 내 모든 데이터 조회
    trends = Trend.objects.all()

    # 그래프를 그리기 위해 x축, y축 리스트 생성
    x_lst = []
    y_lst = []
    
    # 각 데이터마다 키워드(name)는 x축, 검색결과(result)는 y축 리스트에 저장
    for trend in trends:
        x_lst.append(trend.name)
        y_lst.append(trend.result)
    
    # 그래프 생성
    plt.bar(x_lst, y_lst)
    plt.title('Technology Trend Analysis')
    plt.ylabel('Result')
    plt.xlabel('Keyword')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend('Trends')
    
    # 그래프 이미지 저장
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}',
    }
    
    return render(request, 'trends/crawling_histogram.html', context)


# crawling_advanced
# crawling + crawling_histogram
# 검색 기간 제한을 위해 url 추가
def crawling_advanced(request):
    # 키워드 전체 조회
    keywords = Keyword.objects.all()
    
    # Trend table에 저장
    for keyword in keywords:
        trend = Trend.objects.filter(name=keyword.name)
        url = f'https://www.google.com/search?q={keyword.name}&tbs=qdr:y'
        # tbs=qdr:y < 1년
        # tbs=qdr:m < 1달
        # ...
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        result_stats = int(soup.select_one('div#result-stats').text.split()[2][0:-1].replace(',',''))
        temp = Trend.objects.filter(name=keyword.name).count()
        if temp:
            trend = Trend.objects.filter(name=keyword.name)
            trend.result = result_stats
        else:
            trend = Trend(name=keyword.name, result = result_stats, search_period = 'year')
        trend.save()
    
    # 히스토그램 생성
    trends = Trend.objects.all()
    x_lst = []
    y_lst = []
    for trend in trends:
        x_lst.append(trend.name)
        y_lst.append(trend.result)
    plt.bar(x_lst, y_lst)
    plt.title('Technology Trend Analysis')
    plt.ylabel('Result')
    plt.xlabel('Keyword')
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend('Trends')
    
    # 그래프 이미지 저장
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()
    
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'trends/crawling_advanced.html', context)