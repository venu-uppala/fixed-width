"""
    Name: conftest.py
    Author: Venu Uppala
    purpose: Used to define reusable fixtures
"""
from pytest import fixture


@fixture
def valid_record():
    return [1, "TWO", 3, 4, 5, 6, 7, 8, 9, 10]


@fixture
def empty_record():
    return []


@fixture
def invalid_record():
    return [1, 10]


@fixture()
def values_greater_than_spec():
    return ['abcdef', 'abcdefghijklm', 'abcd', 'abc', 'abcdefghijklmn', 'abcdefgh',
                'abcdefghijk', 'abcdefghijklno', 'abcdefghijabcdefghijk', 'abcdefghijklop']

