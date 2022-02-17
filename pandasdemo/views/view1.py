from django.shortcuts import HttpResponse
import pandas as pd
from ..models import *

def home(request):
     df1 = pd.read_csv("data.csv",encoding="ISO-8859-1")
     data.object = df1.to_html()
     return HttpResponse(data.object)