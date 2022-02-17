from django.http import HttpResponse
from django.shortcuts import HttpResponse
from ..models import *
import pandas as pd

def groupData(request):
    df = pd.read_csv("data.csv",encoding="ISO-8859-1")
    gb = df['Occupation'].groupby(df['Sex'])
    return HttpResponse(gb)
