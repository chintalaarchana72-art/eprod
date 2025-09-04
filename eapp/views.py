from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers import ProductSerializer
from .models import Product
                             
# Create your views here.

class ProductList(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
