
class Helicopter:
    
    def __init__(self, full_fuel: int) -> None:
        self.countOfFuel = full_fuel
        self.full = full_fuel
        self.ground = True
    
    def get_amountOfFuel(self) -> str:
        return f"Amount of fuel is {self.countOfFuel}."
    
    def onTheGround(self) -> str:
        return f"Helicopter on the ground: {self.ground}."
    
    def fly(self) -> None:
        if not self.ground:
            print(f"Helicopter is already flying.")
        
        elif self.countOfFuel <= 10:
            print(f"Helicopter doesn't have enough fuel.")
        
        else:
            self.ground = False
            print(f"The helicopter took off.")
            self.countOfFuel -= 10    
    
    def wild(self) -> None:
        if self.ground:
            print(f"The helicopter on the ground.")
        
        else:
            self.ground = True
            print(f"The Helicopter went down.")
    
    def refuel(self, count: int) -> None:
        if not self.ground:
            print(f"The helicopter is flying.")
            
        elif 95 <= self.countOfFuel <= self.countOfFuel:
            print(f"Fuel is full.")
             
        elif 5 <= count <= self.countOfFuel:
            self.countOfFuel += count
            if self.countOfFuel > self.full:
                self.countOfFuel = self.full
                
        else:
            print(f"You must refuel into (5,{self.countOfFuel})")
helicopter = Helicopter(20)
print(helicopter.get_amountOfFuel())
helicopter.fly()
print(helicopter.get_amountOfFuel())
helicopter.refuel(30)    
print(helicopter.get_amountOfFuel())
helicopter.refuel(10)        