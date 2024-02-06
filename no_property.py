from abc import ABC


class Clown:
    def __init__(self):
        self._makeup = "Off"

    def get_makeup(self) -> str:
        return self._makeup

def main():
    clown = Clown()
    print(clown.get_makeup())
    


if __name__=='__main__': 	
    main()