#!/usr/bin/env python3
"""Tests for the Lengths assignment."""

import inspect
import re
import unittest

from src.lengths import lengths


def _source_rows(func: callable):
    """Count the non-blank, non-comment source lines of a function body."""
    src = inspect.getsource(func)
    lines = [
        line.strip()
        for line in re.split(r'\n|;', src)
        if len(line.strip()) > 0 and not line.strip().startswith("#")
    ]
    return len(lines)


class TestLengths(unittest.TestCase):
    """lengths(lists) -> list of the length of each sublist."""

    def test_function_exists(self):
        try:
            from src.lengths import lengths as _lengths
        except Exception as e:
            self.fail(
                "Your program should contain a function named lengths. "
                "Import failed with: %s" % (e,)
            )

    def test_type_of_return_value(self):
        try:
            val = lengths([[1]])
        except Exception as e:
            self.fail(
                "Function threw an error when it was called as follows:\n"
                "lengths([[1]]):\n%s" % (e,)
            )
        self.assertIsInstance(
            val,
            list,
            msg="lengths([[1]]) is expected to return a value which is of "
            "type list, but got %r which is of type %s."
            % (val, type(val).__name__),
        )

    def test_length_of_function(self):
        lines = _source_rows(lengths)
        max_lines = 2
        self.assertLessEqual(
            lines,
            max_lines,
            msg="Function lengths must have at most %d rows in this "
            "exercise (excluding blank rows and comments). The function now "
            "has a total of %d rows. This exercise expects a one-line "
            "list-comprehension solution." % (max_lines, lines),
        )

    def test_with_two_short_sublists(self):
        test_case = [[1, 2], [3, 4]]
        corr = [2, 2]
        val = lengths(test_case)
        self.assertEqual(
            val,
            corr,
            msg="lengths(%r) should return %r, got %r."
            % (test_case, corr, val),
        )

    def test_with_uneven_sublists(self):
        test_case = [[1, 2, 3], [4, 3, 2, 1], [1, 2, 1, 2, 1, 2]]
        corr = [3, 4, 6]
        val = lengths(test_case)
        self.assertEqual(
            val,
            corr,
            msg="lengths(%r) should return %r, got %r."
            % (test_case, corr, val),
        )

    def test_with_repeated_sublist_lengths(self):
        test_case = [[1, 2, 3, 1, 2, 3], [1, 2, 3, 4, 5, 4, 3, 2, 1], [1], [1]]
        corr = [6, 9, 1, 1]
        val = lengths(test_case)
        self.assertEqual(
            val,
            corr,
            msg="lengths(%r) should return %r, got %r."
            % (test_case, corr, val),
        )

    def test_empty_sublists_count_as_zero(self):
        test_case = [[1, 2, 3, 4, 5], [324, -1, 31, 7], []]
        corr = [5, 4, 0]
        val = lengths(test_case)
        self.assertEqual(
            val,
            corr,
            msg="lengths(%r) should return %r: an empty sublist has length "
            "0, got %r." % (test_case, corr, val),
        )

    def test_no_lists_gives_an_empty_result(self):
        val = lengths([])
        self.assertEqual(
            val,
            [],
            msg="lengths([]) should return [] when there are no sublists to "
            "measure, got %r." % (val,),
        )


if __name__ == '__main__':
    unittest.main()
