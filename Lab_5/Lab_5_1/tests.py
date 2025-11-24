import pytest
from functions import (
    count_words,
    find_unique,
    is_palindrome,
    are_anagrams,
    combine_dicts
)


def test_count_words_basic():
    assert count_words("Hello world") == 2

def test_count_words_extra_spaces():
    assert count_words("  Hello   world  again ") == 3

def test_count_words_empty():
    assert count_words("") == 0



def test_find_unique_basic():
    assert find_unique([1, 2, 2, 3, 4, 4]) == [1, 3]

def test_find_unique_all_unique():
    assert find_unique([1, 2, 3]) == [1, 2, 3]

def test_find_unique_none():
    assert find_unique([5, 5, 5]) == []

def test_find_unique_empty():
    assert find_unique([]) == []



def test_is_palindrome_word():
    assert is_palindrome("level") is True

def test_is_palindrome_number():
    assert is_palindrome(1221) is True

def test_is_not_palindrome():
    assert is_palindrome("hello") is False



def test_are_anagrams_basic():
    assert are_anagrams("listen", "silent") is True

def test_are_anagrams_with_spaces():
    assert are_anagrams("a gentleman", "elegant man") is True

def test_are_not_anagrams():
    assert are_anagrams("hello", "world") is False



def test_combine_dicts_basic():
    assert combine_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}

def test_combine_dicts_override():
    assert combine_dicts({"a": 1}, {"a": 3}) == {"a": 3}

def test_combine_dicts_empty():
    assert combine_dicts({}, {"x": 10}) == {"x": 10}
