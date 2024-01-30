def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print("Found")
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
        
    # Target value not found
    return print("Not found")
arr = [5,6,9,14,20]
binary_search(arr, 15)