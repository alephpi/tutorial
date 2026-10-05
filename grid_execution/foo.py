import argparse

from tqdm import tqdm


def concat(args):
    a = args.first
    b = args.second
    for i in tqdm(range(1000)):
        pass
    print(f"first string {a}, second string {b}, concatenated string {a+b}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=str)
    parser.add_argument("--second", type=str)
    args = parser.parse_args()
    concat(args)
if __name__ == "__main__":
    main()
