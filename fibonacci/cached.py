cached = {}

def fibonacci_cached(n: int) -> int:

    if n in cached:
        return cached[n]

    elif n == 0 or n == 1:
        return 1

    else:
        fn = fibonacci_cached(n-2) + fibonacci_cached(n-1)
        cached[n] = fn
        return fn


