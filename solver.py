#!/usr/bin/env python3
"""Script for solving math. Yes, math. All of it.

Usage:

    solver.py 1 + 1

"""

import re
import sys


def solve(equation_str):
    digits = re.split(r'[\s\+]+', equation_str)
    return sum(int(x) for x in digits)


def main(equation_str=None):
    if not equation_str:
        equation_str = ' '.join(sys.argv[1:])
    result = solve(equation_str)
    print(result)

if __name__ == '__main__':
    main()
