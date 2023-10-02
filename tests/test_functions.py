from solutions.functions import *

import pytest

def test_square():
    assert square(5) == 25
    assert square(-5) == 25
    assert square(0) == 0
    assert square(3.5) == 12.25

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("") == ""

def test_find_maximum():
    assert find_maximum([1, 2, 3, 4, 5]) == 5
    assert find_maximum([-1, -2, -3, -4, -5]) == -1
    assert find_maximum([5]) == 5

def test_odd_or_even():
    assert odd_or_even(4) == "Even"
    assert odd_or_even(7) == "Odd"
    assert odd_or_even(0) == "Even"

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False

def test_calculate_area():
    assert calculate_area("circle", 5) == math.pi * 5 * 5
    assert calculate_area("rectangle", 4, 5) == 20
    assert calculate_area("triangle", 3, 4) == 0.5 * 3 * 4

