def linear_search(elements, key):
    size = len(elements)
    Flag = False
    for i in range(size):
        if key == elements[i]:
            Flag = True
            break

    if Flag is True:
        print('Element is found at index ', i)

    else:
        print('Key not found')


if __name__ == '__main__':
    elements = [1, 5, 21, 3, 0]
    linear_search(elements, 1)

