from abc import ABC, abstractmethod

class Star(ABC):
    @abstractmethod
    def Explode() -> None:
        pass
    
    @abstractmethod
    def Implode() -> None:
        pass

class Planet(Star):
    def Explode(self) -> None:
        print("This Planet Has Exploded")
    
    def Implode(self) -> None:
        print("This Planet Has Imploded")

class Moon(Star):
    def Explode(self) -> None:
        print("This Moon Has Exploded")
    
    def Implode(self) -> None:
        print("This Moon Has Imploded")


def main():
    planet = Planet()
    planet.Explode()

    moon = Moon()
    moon.Implode()

if __name__=='__main__': 	
    main()