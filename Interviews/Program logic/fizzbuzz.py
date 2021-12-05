def fizzbuzz(n):

    for i in range(n):
        if i % 3 == 0 & i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:  # divisible by 2
            print("fizz")
        elif i % 5 == 0:  # divisible by 3
            print("buzz")
        else:
            print(str(i))


fizzbuzz(20)
