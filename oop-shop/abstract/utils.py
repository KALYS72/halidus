# def product_update():
#     p_id = int(input('inter id for delete product:'))
    # found = False
    # for product in Product.objects:
    #     if product.id == p_id:
    #         found = True
    #         break
#     if not found:
#         print('product not found')
#     else:
#         field = input('inter area for change: ')
#         if field in dir(product):
#             value = input(f'{field} = ')
#             field_type = type(getattr(product, field))
#             setattr(product, field, field_type(value))

def get_obj_or_404(model, field, value):
    found = False
    for product in model.objects:
        if getattr(product, field) == value:
            found = True
            break
    
    if not found:
        raise Exception(f'404: {model.__name__} c {field} {value} не найден')
    return product
