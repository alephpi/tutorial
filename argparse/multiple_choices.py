from argparse import ArgumentParser


def order(args):
    color = []
    if "apple" in args.fruits:
        color.append('red')
    if "banana" in args.fruits:
        color.append('yellow')
    if "orange" in args.fruits:
        color.append('orange')
    
    return ' '.join(color)

def main():
    parser = ArgumentParser()
    parser.add_argument("--fruits", nargs="+", choices=["apple", "banana", "orange"])
    args = parser.parse_args()
    print(order(args))


if __name__ == "__main__":
    main()