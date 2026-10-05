def parser_b():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", help="stage b")
    parser.add_argument("-d", action="store_true", help="stage b debug")
    return parser


def main():
    parser = parser_b()
    args, _ = parser.parse_known_args()
    print(f"Hello, stage b {args}")

if __name__ == "__main__":
    main()