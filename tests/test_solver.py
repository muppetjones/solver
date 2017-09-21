#!/usr/bin/env python3
"""Tests for the solver module."""

import unittest

import solver as MOD


class TestSolver(unittest.TestCase):

    def test_solve_returns_integer_solution_to_equation_string(self):
        found = MOD.solve('1 + 1')
        expected = 2
        self.assertEqual(found, expected)
