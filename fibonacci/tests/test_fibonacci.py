import pytest
from typing import Callable

from fibonacci.naive import fibonacci_naive
from fibonacci.cached import fibonacci_cached


@pytest.mark.parametrize("m, result", [(0, 0), (1, 1), (2, 1), (20, 6765), ], )
def test_fibonacci_naive(m: int, result: int) -> None:
    res = fibonacci_naive(n=m)
    assert res == result

@pytest.mark.parametrize("m, result", [(0, 0), (1, 1), (2, 1), (20, 6765), ], )
def test_fibonacci_cached(m: int, result: int) -> None:
    res = fibonacci_cached(m)
    return res == result

@pytest.mark.parametrize("func", [fibonacci_naive, fibonacci_cached], )
@pytest.mark.parametrize("m, result", [(0, 0), (1, 1), (2, 1), (20, 6765), ], )
def test_fibonacci(func: Callable[[int], int], m: int, result: int) -> None:
    res = fibonacci_naive(m)
    assert res == result