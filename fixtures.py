from datetime import datetime, timedelta
from typing import Callable

import pytest


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    time_taken = tock - tick
    print(f" Time taken: {time_taken.total_seconds()}")


class PerformanceException(Exception):

    def __init__(self, runtime: timedelta, time_limit: timedelta):
        self.runtime = runtime
        self.time_limit = time_limit

    def __str__(self):
        return f"PerformanceException occurred.  Test time: {self.runtime} is greated than time limit {self.time_limit}"

def track_performance(method: Callable, runtime_limit=timedelta(seconds=1)) -> Callable:
    def run_performance_trancking(*args, **kwargs) -> None:
        tick = datetime.now()

        result = method(*args, **kwargs)

        tock = datetime.now()
        time_taken = tock - tick
        print(f" Time taken: {time_taken.total_seconds()}")

        if time_taken > runtime_limit:
            raise PerformanceException(runtime=time_taken, time_limit=runtime_limit)

        return result

    return run_performance_trancking