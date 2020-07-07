import pytest
from .solution import is_palindrome


@pytest.mark.parametrize(['x', 'result'], [
    [121, True],
    [10, False],
    [-121, False]
])
def test_is_palindrome(x: int, result: bool) -> None:
    assert is_palindrome(x) == result
