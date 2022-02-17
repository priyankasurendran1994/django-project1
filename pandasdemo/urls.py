from django.urls import url
from .views import viewsa

urlpatterns = [
    url(r'^aaa$', views, name='view_a'),
    
]