from rest_framework import serializers
from .models import Product, ProductAccessRequest, Lesson

class ProductSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Product
        fields = "__all__"

class ProductAccessRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccessRequest
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
