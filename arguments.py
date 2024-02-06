import argparse as ap

def main() -> None:
    parser = ap.ArgumentParser()
    parser.add_argument(dest='words', help='Give a String', type=str)
    parser.add_argument(dest='iNum', help='Give an Integer', type=int)
    parser.add_argument(dest='fNum', help='Give a Float', type=float)

    args = parser.parse_args()

    words=args.words
    iNums=args.iNum
    fNums=args.fNum

    print("String: ", words)
    print("Integer: ", iNums)
    print("Float: ", fNums)

if __name__=='__main__': 	
    main()