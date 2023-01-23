class ShoppingCart:
    
    def __init__(self):
        self.cart = []
    
    def add_product(self, product):
        self.cart.append(product)
    
    def remove_product(self, product):
        self.cart.remove(product)
    
    def get_cart(self):
        return self.cart
    
    def __str__(self):
        return f"{self.cart}"
                        