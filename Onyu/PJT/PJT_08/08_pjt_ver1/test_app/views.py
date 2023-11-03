# from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
csv_path = './data/test_data.CSV'
csv_null = './data/test_data_has_null.CSV'
# Create your views here.


def csv_to_df(request):
    dataframe = pd.read_csv(csv_path, encoding='cp949')
    data = dataframe.to_dict('records')
    context = {
        'dataframe' : data
    }
    return JsonResponse(context)


def handle_null(request):
    # 결측치 처리 후 데이터 반환
    dataframe = pd.read_csv(csv_null, encoding='cp949')
    dataframe = dataframe.fillna('Null')
    # print(dataframe)
    data = dataframe.to_dict('records')
    context = {
        'df' : data  
    }
    return JsonResponse(context)


def age_avg(request):
    Df = pd.read_csv(csv_null, encoding='cp949')
    Df = Df.dropna(subset=['나이'])
    avg_df = int(Df['나이'].mean())
    Df['차이'] = abs((Df['나이'] - avg_df))
    Df = Df.sort_values(by='차이')
    res = Df.head(10)
    res = res.to_dict('records')
    return JsonResponse({'msg' : res})


def age_avg2(request):
    data = np.genfromtxt('./data/test_data_has_null.csv', delimiter=',',dtype=None, encoding='cp949')
    # print(data[1])
    # meanNP = np.mean(data, axis=0)
    # print(meanNP)
    data = data.tolist()
    # print(data)
    data[0][1] = '평균과의 차이'
    data = data[1:]
    t_sum = 0
    cnt = 0
    for i in data:
        if not i[1]:
            i[1]= 9999999
        else:
            t_sum += int(i[1])
            cnt += 1
    avg = t_sum // cnt
    for i in data:
        i[1] = abs(int(i[1])-avg)
    data.sort(key=lambda x:x[1])
    res = data[:10]
    return JsonResponse({'result' : res})
    
    # print(type(data[13][1]))
    # data = np.isnan(data)
    # dataMean = np.nanmean(data, axis=0)
    return JsonResponse({1:1})

