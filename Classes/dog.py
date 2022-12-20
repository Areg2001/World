
class Dog:

    def __init__(self, name: str) -> None:
        self.name = name
        self.energy = 100
        self.sleep = False

    def isSleeping(self) -> bool:
        return self.sleep

    def barks(self) -> None:
        if self.sleep:
            print(f"{self.name} is sleeping.")

        elif self.energy <= 5:
            self.sleep = True

        else:
            self.energy -= 5

    def running(self) -> None:
        if self.sleep:
            print(f"{self.name} is slepping.")

        elif self.energy <= 20:
            self.sleep = True

        else:
            self.energy -= 20

    def dogWakeUp(self) -> None:
        if not self.sleep:
            print(f"{self.name} is already active.")
            
        else:
            self.sleep = False
            self.energy = 100
 
    def eating(self) -> None:
        if self.sleep:
            print(f"{self.name} is slepping.")
            
        elif self.energy <= 90:
            self.energy += 10
        
        else:
            print(f"{self.name} is full.")
    
    def get_energy(self) -> str:
        return f"{self.name} energy is {self.energy}."
    
    def get_name(self) -> str:
        return f"Dog's name is {self.name}."

          
        