# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# odd_squares = []
# for number in numbers:
#     if number % 2 != 0:
#         odd_squares.append(number * number)
#
# print(odd_squares)

# Варіант 2


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda number: number % 2 != 0, numbers))
odd_squares = list(map(lambda number: number * number, odd_numbers))

print(odd_squares)