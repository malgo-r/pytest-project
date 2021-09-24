import time

import pytest

from fixtures import track_performance
from fibonacci.cached import fibonacci_cached


@pytest.mark.performance  # gosia custom marker
@track_performance
def test_fibonacci_cached_performance() -> None:
    time.sleep(2)
    fibonacci_cached(1344)