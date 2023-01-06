class Category:
    objects = []

    def __init__(self, title):
        self.title = title
        Category.objects.append(self)
    
    def __str__(self) -> str:
        return self.title
    
class Product:
    objects = []
    _id = 1

    def __init__(self, title:str, price:float, category:Category):
        self.id = Product._id
        self.title = title
        self.price = price
        self.category = category
        Product.objects.append(self)
        Product._id += 1 

    def __str__(self) -> str:
        return f'{self.category} -> {self.title}'