from dataclasses import dataclass

@dataclass
class Star:
    name: str
    mass: int
    diameter: float

    def implode(self) -> None:
        self.mass /= 10
        self.diameter /= 20

    def collide(self, star: object) -> None:
        self.mass += star.mass
        self.diameter += star.diameter

def main():

    
    sol = Star("Sol", 1000, 225)
    proximaCentauri = Star("Proxima Centauri", 300, 70)

    print("Before Implosion:")
    print(" Name: " + sol.name)
    print(" Mass: " + str(sol.mass))
    print(" Diameter: " + str(sol.diameter))
    print()

    sol.implode()

    print("After Implosion:")
    print(" Name: " + sol.name)
    print(" Mass: " + str(int(sol.mass)))
    print(" Diameter: " + str(sol.diameter))
    print()

    print("Before Collision:")
    print(" Name: " + proximaCentauri.name)
    print(" Mass: " + str(proximaCentauri.mass))
    print(" Diameter: " + str(proximaCentauri.diameter))
    print()

    proximaCentauri.collide(sol)

    print("After Collision:")
    print(" Name: " + proximaCentauri.name)
    print(" Mass: " + str(int(proximaCentauri.mass)))
    print(" Diameter: " + str(proximaCentauri.diameter))


if __name__=='__main__': 	
    main()