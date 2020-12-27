import argparse
from ._version import __version__


def main(parser=argparse.ArgumentParser()):

    print("Executing 'main()' from my app!")
    parser.add_argument(
        "-v", "--version", action="store_true", help="Shows the app version."
    )
    parser.add_argument(
        "-s", "--square", type=int, required=False, help="Square a number."
    )

    args = parser.parse_args()

    if args.version:
        return __version__
    elif args.square:
        return square(args.square)
    else:
        return "Hello World"


def square(x: int):
    y = x * x
    print(f"The square of {x} is {y}!")
    return y
