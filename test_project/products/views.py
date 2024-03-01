from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.contrib.auth.decorators import permission_required
from rest_framework.response import Response

from .models import Product, ProductAccessRequest, Lesson
from rest_framework import generics, status
from .serializers import ProductSerializer, ProductAccessRequestSerializer, LessonSerializer

class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LessonAPIList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser, )

class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAccessRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductAccessRequest.objects.all()
    serializer_class = ProductAccessRequestSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

