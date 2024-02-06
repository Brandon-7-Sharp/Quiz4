from abc import ABC, abstractmethod
import argparse as ap
# from dataclasses import dataclass

# @dataclass
class Star:
    @abstractmethod
    def Explode() -> None:
        pass
    
    @abstractmethod
    def Implode() -> None:
        pass

# @dataclass
class Planet(Star):
    def Explode(self) -> None:
        print("This Planet Has Exploded")
    
    def Implode(self) -> None:
        print("This Planet Has Imploded")

# @dataclass
class Moon(Star):
    def Explode(self) -> None:
        print("This Moon Has Exploded")
    
    def Implode(self) -> None:
        print("This Moon Has Imploded")


def main():

    parser = ap.ArgumentParser()
    parser.add_argument(dest='Terra', help='1 = Explode, 2 = Implode', type=int)
    parser.add_argument(dest='Luna', help='1 = Explode, 2 = Implode', type=int)

    args = parser.parse_args()

    planet=args.Terra
    moon=args.Luna

    terra = Planet()
    if (planet == 1):
        terra.Explode()
    else:
        terra.Implode()

    luna = Moon()
    if (moon == 1):
        luna.Explode()
    else:
        luna.Implode()

if __name__=='__main__': 	
    main()