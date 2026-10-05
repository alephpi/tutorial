def parser_a():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", help="stage a")
    parser.add_argument("-d", action="store_true", help="stage a debug")
    return parser

def main():
    parser = parser_a()
    args, _ = parser.parse_known_args()
    print(f"Hello, stage a {args}")

if __name__ == "__main__":
    main()
