from cart import ShoppingCart

class User:
    
    def __init__(self, name: str, id: int, email: str) -> None:
        self.__name = name
        self.__id = id
        self.__email = email
        self.__money = 5000000
        self.__cart = ShoppingCart()
    
    def get_name(self) -> None:
        print(f"Name: {self.__name}")
    
    def get_id(self) -> None:
        print(f"Id: {self.__id}")
    
    def get_email(self) -> None:
         print(f"email: {self.__email}")
    
    def get_cart(self) -> None:
        print(f"Cart: {self.__cart.get_cart()}")

    def get_money(self) -> None:
        print(f"Money: {self.__money}")       
    
    def add_money(self, money: int) -> None:
        self.__money += money

    def set_name(self, new_name: str) -> None:
        self.__name = new_name
    
    def set_email(self, new_email: str) -> None:
        self.__email = new_email
    
    def set_id(self, new_id: int) -> None:
        self.__id = new_id
    
    def add_product(self, product) -> None:
        self.__cart.add_product(product.name)    
    
    def remove_product(self, product) -> None:
        self.__cart.remove_product(product)

    def buy_product(self, product) -> None:
        if product.name in self.__cart.get_cart():
            self.__money -= product.price
            self.__cart.remove_product(product)

        else:
            print("You must add it in shopping-cart: ")    
    
    def __str__(self) -> str:
        return f"{self.__name}, {self.__id}, {self.__email}, {self.__cart}"