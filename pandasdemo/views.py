from django.http import HttpResponse
from django.shortcuts import HttpResponse
from .models import *
import pandas as pd



def home(request):
     df1 = pd.read_csv("C:/Users/S.PRIYANKA/demo/firstapp/data.csv",encoding="ISO-8859-1")
     data.object = df1.to_html()
     return HttpResponse(data.object)

def groupData(request):
    df = pd.read_csv("C:/Users/S.PRIYANKA/demo/firstapp/data.csv",encoding="ISO-8859-1")
    gb = df['Occupation'].groupby(df['Sex'])
    return HttpResponse(gb)
