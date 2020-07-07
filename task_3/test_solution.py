import pytest
from .solution import length_of_longest_substring


@pytest.mark.parametrize(['s', 'length'], [
    ['', 0],
    ['aab', 2],
    ['bbbbb', 1],
    ['abcabccbb', 3],
    ['pwwkew', 3],
    ['abcadefgabc', 7],
    ['abcdefg', 7]
])
def test_length_of_longest_substring(s: str, length: int):
    assert length_of_longest_substring(s) == length
