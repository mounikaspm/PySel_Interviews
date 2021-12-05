l1 = [1, 2, 3, 4, 5, 6]

n = 5
for k in range(1, 4):
    for i in range(0, 5):
        first = l1[0]
        for j in range(0, len(l1) - 1):
            l1[j] = l1[j + 1]

        l1[len(l1) - 1] = first

    print(l1)


