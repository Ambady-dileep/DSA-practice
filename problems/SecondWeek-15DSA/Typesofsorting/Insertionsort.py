       
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        print(f"Key is {key} at index {i}")
        j = i - 1
        while j >= 0 and arr[j] > key:
            print(f"{arr[j]} > {key} -> shifting {arr[j]} to position {j + 1}")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Inserted key at position {j + 1} -> {arr}")
    return arr

arr = [5, 3, 2, 1]
print("Final Sorted Array:", insertion_sort(arr))