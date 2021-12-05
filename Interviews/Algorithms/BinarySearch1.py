def binary_search(elements, key):
    a = elements
    size = len(elements)
    low = 0
    high = size - 1

    while low <= high:

        mid = (low + high) // 2

        if key == a[mid]:
            return 'Element found at index: ' + str(mid)

        elif key < a[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return False


if __name__ == "__main__":
    elements = [1, 2, 5, 9, 34, 34, 67, 88]
    print(binary_search(elements, 2))
