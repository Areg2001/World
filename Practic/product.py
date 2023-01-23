class Product:
    
    def __init__(self, name, price, features):
        self.name = name
        self.price = price
        self.features = features
        
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_features(self):
        return self.features    
    
    def set_name(self, newname):
        self.name = newname
    
    def set_price(self, new_price):
        self.price = new_price
    
    def set_features(self, new_features):
        self.features = new_features      

    def get_product(self):
        return f"{self.name}, {self.price}, {self.features}"
    
    def __str__(self):
         return f"{self.name}, {self.price}, {self.features}"          