from abc import ABC


class Clown:
    def __init__(self):
        self._makeup = "On"

    @property
    def makeup(self) -> str:
        return self._makeup

def main():
    clown = Clown()
    print(clown.makeup)
    


if __name__=='__main__': 	
    main()