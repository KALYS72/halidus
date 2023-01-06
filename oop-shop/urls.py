from shop.views import *

urlpatterns = [
    ('products', product_list),
    ('create', create_product),
    ('delete', delete_product),
    ('update', product_update),
    ('details', product_detale)
]