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

        if self.energy <= 5:
            self.sleep = True

        else:
            self.energy -= 5

    def running(self) -> None:
        if self.sleep:
            print(f"{self.name} is slepping.")

        if self.energy <= 20:
            self.sleep = True

        else:
            self.energy -= 20


    def dogWakeUp(self) -> None:
        self.sleep = False
        self.energy = 100

dog = Dog("Jack")
dog.running()
dog.running()
dog.running()
dog.running()
print(dog.isSleeping())
dog.running()
print(dog.isSleeping())
dog.barks()
dog.dogWakeUp()
print(dog.isSleeping())
dog.barks()

