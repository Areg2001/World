from cart import ShoppingCart
from product import Product

class User:
    
    def __init__(self, name, id, email):
        self.__name = name
        self.__id = id
        self.__email = email
        self.__cart = ShoppingCart()
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_email(self):
        return self.__email
    
    def get_cart(self):
        return self.__cart.get_cart()   
    
    def set_name(self, new_name):
        self.__name = new_name
    
    def set_email(self, new_email):
        self.__email = new_email
    
    def set_id(self, new_id):
        self.__id = new_id
    
    def add_product(self, product):
        self.__cart.add_product(product.name)    
    
    def buy_product(self, product):
        self.__cart.remove_product(product)
    
    def __str__(self):
        return f"{self.__name}, {self.__id}, {self.__email}, {self.__cart}"
