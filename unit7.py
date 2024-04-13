def multiply(x, y):

    return x * y

result = multiply(5, 3)
print(result)

def multiply_curry(x):

    def inner(y):
        return x * y
    return inner


multiply_5 = multiply_curry(5)


# result = multiply_5(3)
# print(result)


multiply = multiply_curry(5)(3)


# result = multiply_5(3)
# print(result)