from .models import Product, Category
from .serializers import ProductSerializer
from abstract.utils import get_obj_or_404
from pprint import pprint


def product_list():
    serializer = ProductSerializer()
    pprint(serializer.serialize_objects())

def create_product():
    title = input('Введите название: ')
    price = float(input('Введите цену: '))
    print('Выберите категорию:')
    for category in Category.objects:
        print(category.title)
    cat_title = input()
    cat = get_obj_or_404(Category, 'title', cat_title)
    Product(title, price, cat)
    

def delete_product():
    p_id = int(input('inter id for delete product:'))
    product = get_obj_or_404(Product, 'id', p_id)
    Product.objects.remove(product)
        

def product_detale():
    p_id = int(input('inter id for delete product:'))
    product = get_obj_or_404(Product, 'id', p_id)
    serializer = ProductSerializer()
    print(serializer.serialize_obj(product))

    
def product_update():
    p_id = int(input('inter id for delete product:'))
    product = get_obj_or_404(Product, 'id', p_id)
    field = input('inter area for change: ')
    if field in dir(product):
        value = input(f'{field} = ')
        field_type = type(getattr(product, field))
        setattr(product, field, field_type(value))


cat1 = Category('some Category')
Product('1 product', 34.0, cat1)
Product('2 product', 29.5, cat1)

