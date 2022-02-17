from xml.etree.ElementInclude import include
from django import views
from django.urls import path
from pandasdemo.views import view1,view2

urlpatterns = [
    path('',view1.home,name="home"),
    path('groupData',view2.groupData,name="groupData")
   # path('groupData',views.groupData,name="groupData")
]


