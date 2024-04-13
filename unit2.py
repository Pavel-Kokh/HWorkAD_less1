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

@timer
def my_function(n):

    for i in range(n):
        print(i)

    my_function(1000)