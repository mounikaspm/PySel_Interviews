# fib of 5 numbers

# o/p: 01123

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)


n = 5
for n in range(0, n + 1):
    print(fibonacci(n))

