# def fibonacci(n):
#
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
# for i in range(25):
#   print(fibonacci(i))


 # """ З кешем довільної довжини"""

# import functools
# def fibonacci_with_cache(n):
#     cache = {}
#
# @functools.lru_cache()
# def wrapper(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return wrapper(n - 1) + wrapper(n - 2)
#
#     return wrapper(n)
#
# for i in range(25):
#     print(fibonacci_with_cache(i))


                # З кешем з модулю functools з максимальною кількістю 10 елементів

# import functools
#
# def fibonacci_with_cache_10(n):
#
#     @functools.lru_cache(maxsize=10)
#     def wrapper(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return wrapper(n - 1) + wrapper(n - 2)
#
#     return wrapper(n)
#
#
# for i in range(25):
#     print(fibonacci_with_cache_10(i))


#               З кешем з модулю functools з максимальною кількістю 16 елементів


# import functools
#
# def fibonacci_with_cache_16(n):
#
#     @functools.lru_cache(maxsize=16)
#     def wrapper(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return wrapper(n - 1) + wrapper(n - 2)
#
#     return wrapper(n)
#
# for i in range(25):
#     print(fibonacci_with_cache_16(i))


