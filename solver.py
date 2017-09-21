#!/usr/bin/env python3
"""Script for solving math. Yes, math. All of it.

Usage:

    solver.py 1 + 1

"""

import re
import sys


def solve(equation_str):
    digits = re.split(r'[\s\+]+', equation_str)
    try:
        return sum(int(x) for x in digits)
    except ValueError:
        msg = 'operands must be digits'
        raise ValueError(msg) from None


def main(equation_str=None):
    status_code = 0

    if not equation_str:
        equation_str = ' '.join(sys.argv[1:])

    try:
        result = solve(equation_str)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        status_code = 1
    else:
        print(result)
        status_code = 0
    finally:
        return status_code


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
