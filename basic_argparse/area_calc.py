import argparse
import math
import sys
from pathlib import Path


def calc_area_retangle(a, b):
    return a * b


def calc_area_square(a):
    return a**2


def calc_area_triangle(b, h):
    return b * h / 2


def calc_area_circle(r):
    return math.pi * r**2


def main():
    parser = argparse.ArgumentParser(
        prog="areacalc)",
        description="Area Calculator",
        fromfile_prefix_chars="@",  # arquivos com os parametros pré-fixados
    )

    parser.add_argument("-a", type=int, help="width or radios")
    parser.add_argument("-b", type=int, help="lenght or height")
    parser.add_argument("-v", "--verbose", help="print more detail", action="store_true")
    parser.add_argument("-o", "--output", help="stdout in file", action="store_true")

    contype = parser.add_mutually_exclusive_group(required=True)
    contype.add_argument("-s", "--square", help="Calc area square", action="store_true")
    contype.add_argument("-r", "--retangle", help="Calc area retangle", action="store_true")
    contype.add_argument("-t", "--triangle", help="Calc area triangle", action="store_true")  # on/off flag

    args = parser.parse_args()

    if args.output:
        arq = open("area_calc.txt", "w")
        sys.stdout = arq

    if args.verbose:
        print(f"the a number is {args.a}")
        print(f"the b number is {args.b}")

    if args.square:
        A = calc_area_square(args.a)
        print(f"Square area: {A}")

    elif args.retangle:
        A = calc_area_retangle(args.a, args.b)
        print(f"Retangle area: {A}")

    elif args.triangle:
        A = calc_area_triangle(args.a, args.b)
        print(f"Trianggle area: {A}")


if __name__ == "__main__":
    main()
