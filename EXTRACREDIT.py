def ultimateArrayPrinter(array: []) -> [int]:
    returnArray = []
    for value in array:
        returnArray.append(len(str(value)))
    
    return returnArray

def main():
    array = []
    array = [664, 'gg', 2, 3, 4, 8]

    print(ultimateArrayPrinter(array))

if __name__=='__main__': 	
    main()