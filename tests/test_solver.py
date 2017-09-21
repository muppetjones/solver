#!/usr/bin/env python3
"""Tests for the solver module."""

import unittest
from unittest import mock

import solver as MOD


class TestSolver(unittest.TestCase):

    def test_solve_returns_integer_solution_to_equation_string(self):
        found = MOD.solve('1 + 1')
        expected = 2
        self.assertEqual(found, expected)


class TestSolver__main(unittest.TestCase):

    def test_main_calls_solve_with_input(self):
        with mock.patch.object(MOD, 'solve') as mock_solve:
            MOD.main('foo')
        mock_solve.assert_called_once_with('foo')

    def test_joins_argv_input_into_equation_str_if_no_input(self):
        with mock.patch.object(MOD, 'solve') as mock_solve, \
                mock.patch.object(MOD, 'sys') as mock_sys:
            mock_sys.argv = ['foo']
            MOD.main()
        mock_solve.assert_called_once_with('foo')

    def test_main_prints_solve_output(self):
        with mock.patch.object(MOD, 'print') as mock_print, \
                mock.patch.object(MOD, 'solve') as mock_solve:
            MOD.main('foo')

        mock_print.assert_called_once_with(mock_solve.return_value)
