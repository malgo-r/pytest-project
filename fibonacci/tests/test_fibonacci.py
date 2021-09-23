import pytest

from fibonacci.naive import fibonacci_naive


@pytest.mark.parametrize("m, result", [(0, 0), (1, 1), (2, 1), (20, 6765), ],)
def test_fibonacci_naive(m: int, result: int) -> None:
    res = fibonacci_naive(n=m)
    assert res == result
