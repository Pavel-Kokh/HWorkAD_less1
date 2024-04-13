def fibonacci_generator():

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for num in fibonacci_generator():
    if num > 100:
        break
    print(num)

def even_fibonacci_generator(generator):

    for num in generator:
        if num % 2 == 0:
            yield num

even_fibonacci = even_fibonacci_generator(fibonacci_generator())

for num in even_fibonacci:
    if num > 100:
        break
    print(num)