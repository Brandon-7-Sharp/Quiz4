from typing import Protocol
import argparse as ap
import os

class Star(Protocol):
    def Explode(self) -> None:
        pass
    
    def Implode(self) -> None:
        pass

class Planet:
    def __init__(self,filename:str) -> None:
        self.filename = filename

    def save(self,data:str) -> None:
        with open(self.filename,"w") as file:
            file.write(data)

    def load(self)->str:
        with open(self.filename,"r") as file:
            return file.read()


    def Explode(self) -> None:
        print("This Planet Has Exploded")
    
    def Implode(self) -> None:
        print("This Planet Has Imploded")

class Moon:
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

    data = ""

    terra = Planet("data_1.txt")
    if (planet == 1):
        terra.Explode()
        data = "Dynamite"
    else:
        terra.Implode()
        data = "TNT"

    star_check : Star = Planet("data_1.txt")
    star_check.save(data)

    loaded_data = star_check.load()
    print("Cause of Planet Destruction: ", loaded_data)

    luna = Moon()
    if (moon == 1):
        luna.Explode()
    else:
        luna.Implode()

if __name__=='__main__': 	
    main()