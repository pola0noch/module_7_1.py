# Домашнее задание по теме "Режимы открытия файлов"
from pprint import pprint

class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, Вес: {self.weight}, Категория: {self.category}"

class Shop:
    def __init__(self, __file_name = 'products.txt' ):
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, "r")
        file_read = file.read()
        file.close()
        return file_read

    def add(self, *products):
        file = open(self.__file_name, "a")
        for product in products:
            _products = self.get_products()
            product_str = str(product)
            if product_str not in _products:
                file.write(f"{product}\n")
            else:
                print(f"Продукт {product} уже есть в магазине")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())











