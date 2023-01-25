class Product:
    
    def __init__(self, name: str, price: int, features: str) -> None:
        self.name = name
        self.price = price
        self.features = features
        
    def get_name(self) -> None:
        print(self.name)
    
    def get_price(self) -> None:
        print(self.price)
    
    def get_features(self) -> None:
        print(self.features)    
    
    def set_name(self, newname: str) -> None:
        self.name = newname
    
    def set_price(self, new_price: int) -> None:
        self.price = new_price
    
    def set_features(self, new_features: str) -> None:
        self.features = new_features      

    def get_product(self) -> str:
        return f"{self.name}, {self.price}, {self.features}"
    
    def __str__(self) -> str:
         return f"{self.name}, {self.price}, {self.features}"    