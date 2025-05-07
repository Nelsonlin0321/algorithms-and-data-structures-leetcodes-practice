def heapSort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root (max) with last element
        heapify(arr, i, 0)  # Heapify the reduced heap

    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 3, 2, 1, 4, 5, 7, 8]
    sorted_arr = heapSort(arr)
    print(sorted_arr)
