import time

def timer(func):


    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Функція {func.__name__} виконувалась протягом {total_time:.2f} секунд.")
        return result
    return wrapper

# Заміряємо час для кожного варіанту
@timer
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(25):
    print(fibonacci(i))


import functools
@timer
def fibonacci_with_cache(n):

    cache = {}
@functools.lru_cache()
def wrapper(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return wrapper(n - 1) + wrapper(n - 2)

    return wrapper(n)

for i in range(25):
    print(fibonacci_with_cache(i))

@timer
def fibonacci_with_cache_10(n):


    @functools.lru_cache(maxsize=10)
    def wrapper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return wrapper(n - 1) + wrapper(n - 2)

    return wrapper(n)


for i in range(25):
    print(fibonacci_with_cache_10(i))


@timer
def fibonacci_with_cache_16(n):
    @functools.lru_cache(maxsize=16)
    def wrapper(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return wrapper(n - 1) + wrapper(n - 2)

        return wrapper(n)


for i in range(25):
    print(fibonacci_with_cache_16(i))

n = 25
fibonacci(n)
fibonacci_with_cache(n)
fibonacci_with_cache_10(n)
fibonacci_with_cache_16(n)