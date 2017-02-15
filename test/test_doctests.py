#!/usr/bin/env python
# coding: utf-8
import doctest

from picard import metadata


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(metadata))
    return tests
