def bubble_sort(elements):
    a = elements
    size = len(elements)

    for k in range(size-1):
        swapped = False
        for i in range(size - 1 - k):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    bubble_sort(elements)
    #bubble_sort(elements, key=lambda x: x['transaction_amount'])
    print(elements)


