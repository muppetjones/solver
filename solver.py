#!/usr/bin/env python3
"""Script for solving math. Yes, math. All of it.

Usage:

    solver.py 1 + 1

"""

import sys


def solve(equation_str):
    return 2


def main(equation_str=None):
    if not equation_str:
        equation_str = ' '.join(sys.argv)
    result = solve(equation_str)
    print(result)

if __name__ == '__main__':
    main()
