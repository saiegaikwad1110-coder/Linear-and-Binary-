def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Input
arr = list(map(int, input("Enter sorted elements: ").split()))
target = int(input("Enter element to search: "))

# Search
result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")