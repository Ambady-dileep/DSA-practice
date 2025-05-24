# <<--------------------Linear Search------------------------>>

def linear_search(arr,target):
    for i in range(len(arr)):
        print(f"Checking index {i}: {arr[i]}")
        if arr[i] == target:
            print("Target found")
            return i
        print("Target not Found!")
    return -1

arr = [10, 25, 3, 7, 18, 42]
target = 7

index = linear_search(arr,target)
print(f"\nResult: Target found at index {index}")