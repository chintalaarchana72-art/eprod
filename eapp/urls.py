from django.urls import  path
from eapp.views import ProductList

urlpatterns = [
    path('product/',ProductList.as_view()),


    
]