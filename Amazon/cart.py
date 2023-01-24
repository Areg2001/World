from product import Product

class ShoppingCart:
    
    def __init__(self) -> None:
        self.cart = []
    
    def add_product(self, product: Product) -> None:
        self.cart.append(product)
    
    def remove_product(self, product: Product) -> None:
        self.cart.remove(product.name)
    
    def get_cart(self) -> list:
        return self.cart
    
    def __str__(self):
        return f"{self.cart}"