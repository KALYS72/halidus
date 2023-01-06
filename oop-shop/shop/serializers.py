from abstract.serializers import BaseSerializer
from .models import Category, Product


class ProductSerializer(BaseSerializer):
    class Meta:
        fields = ['id', 'title', 'price', 'category']
        objects = Product.objects

    def serialize_obj(self, obj):
        representaiton = super().serialize_obj(obj)
        representaiton['category'] = obj.category.title
        return representaiton