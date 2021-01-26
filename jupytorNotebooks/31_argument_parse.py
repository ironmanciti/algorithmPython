import sys
import argparse

def _parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from_date",
        help="starting date",  # python boilerplate.py -h/--help
        type=str,
        default="2020.01.01"
    )
    parser.add_argument(
        "--to_date",
        help="end date",
        type=str,
        default="2020.12.31"
    )
    return parser.parse_known_args(argv)

def hello():
    print('Hello world to Python programming')

if __name__ == '__main__':
    hello()
    print(sys.argv)
    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[1:])
    
    args = _parse_arguments(sys.argv[1:])[0]
    print(args)
