import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Funkcja '{func.__name__}' wykonana w czasie {end_time - start_time:.6f} sekund.")
        return result
    return wrapper


@timeit
def example_function():
    time.sleep(2)

example_function()
