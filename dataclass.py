from dataclasses import dataclass

@dataclass
class Star:
    name: str
    mass: int
    diameter: float

    def implode(self) -> None:
        self.mass /= 10
        self.diameter /= 20

def main():

    
    sol = Star("Sol", 1000, 225)

    print("Name: " + sol.name)
    print("Mass: " + str(sol.mass))
    print("Diameter: " + str(sol.diameter))

    print()
    sol.implode()

    print("Name: " + sol.name)
    print("Mass: " + str(int(sol.mass)))
    print("Diameter: " + str(sol.diameter))


if __name__=='__main__': 	
    main()