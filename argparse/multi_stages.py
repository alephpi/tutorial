from stage_a import main as main_a
from stage_b import main as main_b

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Multi-stages training')
    # parser.add_argument('-d', action='store_true')
    parser.add_argument('-d')

    args, _ = parser.parse_known_args()
    print(f"gateway {args.d}")
    main_a()
    main_b()