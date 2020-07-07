import pytest

from .solution import longest_palindrome


@pytest.mark.parametrize(['s', 'substr'], [
    ['', ''],
    ['a', 'a'],
    ['aa', 'aa'],
    ['ac', 'a'],
    ['babad', 'bab'],
    ['cbbd', 'bb'],
    ['acvkeek', 'keek'],
    ['aaabaaaa', 'aaabaaa'],
    ['babadddaa', 'addda']
])
def test_longest_palindrome(s: str, substr: str) -> None:
    assert longest_palindrome(s) == substr
