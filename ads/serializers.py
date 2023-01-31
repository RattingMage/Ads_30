from rest_framework import serializers

from ads.models import Ad, Category, Selection
from users.serializers import UserSerializer, UserLocationSerializer


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    author = UserLocationSerializer()

    class Meta:
        model = Ad
        fields = ['name', 'price', 'author', 'category']


class AdDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Ad
        fields = "__all__"
