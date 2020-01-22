"""Tests for `csw` package."""

import pytest
from pkg_resources import parse_version

import csw


def test_valid_version():
    """Check that the package defines a valid ``__version__``."""
    v_curr = parse_version(csw.__version__)
    v_orig = parse_version("0.1.0")
    assert v_curr >= v_orig


def test_file_write():
    t1 = ['x', 'y', '1423', 'randar', 'tzz']
    t1n = ['x', 'y', '1423', 'randar', 'tzz']
    csw.csw('t1', t1, t1n)

    with open('t1-test.txt', r) as test:
        test_output = test.readlines()

    with open('t1.txt', r) as actual:
        actual_output = actual.readlines()

    for test_line, actual_line in zip(test_output, actual_output):
        assert test_line == actual_line

    pass
