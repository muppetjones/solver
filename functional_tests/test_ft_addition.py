#!/usr/bin/env python3
"""Functional testing of addition using solver."""

import os
import subprocess
import unittest

REPO_DIR = os.path.dirname(os.path.dirname(__file__))
SCRIPT_PATH = os.path.join(REPO_DIR, 'solver.py')


class TestSolverAddition(unittest.TestCase):

    def test_solver_prints_solution_to_basic_addition_of_two_numbers(self):
        # Kate is tired. She hates mental math.
        # She decides to give solver a try.
        # Kate calls solver with two numbers.
        cmd = 'python3 {} 1 + 1'.format(SCRIPT_PATH)
        result = subprocess.check_output(cmd.split())

        # She checks the output against the expected answer,
        # is thrilled to find it worked!
        expected = '2'
        self.assertEqual(result, expected)
