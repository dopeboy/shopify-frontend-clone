from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class PingView(APIView):
    def get(self, request, format=None):
        """
        Return 'pong' if it worked.
        """
        return Response({"status": "pong"})


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
