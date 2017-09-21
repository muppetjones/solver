#!/usr/bin/env python3
"""Tests for the solver module."""

import sys
import unittest
from unittest import mock

import solver as MOD


class TestSolver(unittest.TestCase):

    def test_solve_returns_integer_solution_to_equation_string(self):
        test_list = [
            ('1 + 1', 2),
            ('1 + 41', 42),
        ]
        for given, expected in test_list:
            with self.subTest(equation=given):
                found = MOD.solve(given)
                self.assertEqual(found, expected)

    def test_raises_ValueError_if_non_digit_operand_given(self):
        with self.assertRaisesRegex(ValueError, 'operands must be digits'):
            MOD.solve('X + Y')


class TestSolver__main(unittest.TestCase):

    def setUp(self):
        super().setUp()

        patch = mock.patch.object(MOD, 'solve')
        self.mock_solve = patch.start()
        self.addCleanup(patch.stop)

    def test_main_calls_solve_with_input(self):
        MOD.main('foo')
        self.mock_solve.assert_called_once_with('foo')

    def test_joins_argv_input_into_equation_str_if_no_input(self):
        with mock.patch.object(MOD, 'sys') as mock_sys:
            mock_sys.argv = ['script.py', 'foo']
            MOD.main()
        self.mock_solve.assert_called_once_with('foo')

    def test_main_prints_solve_output(self):
        with mock.patch.object(MOD, 'print') as mock_print:
            MOD.main('foo')
        mock_print.assert_called_once_with(self.mock_solve.return_value)

    def test_main_prints_ValueError_message_if_solve_fails(self):
        self.mock_solve.side_effect = ValueError('foo')
        with mock.patch.object(MOD, 'print') as mock_print:
            MOD.main('bar')  # should not raise!
        mock_print.assert_called_once_with('foo', file=sys.stderr)
