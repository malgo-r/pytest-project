def fibonacci_naive(n: int) -> int:
    if n > 1:
        return fibonacci_naive(n - 2) + fibonacci_naive(n - 1)
    else:
        return n
