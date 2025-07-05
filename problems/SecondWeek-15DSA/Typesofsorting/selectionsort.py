# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+n,n):
#             if arr[j]<arr[min_index]:
#                 min_index = j
#         arr[i],arr[min_index]= arr[min_index],arr[i]
#     return arr 

# arr = [4,2,7,1]
# print(selection_sort(arr))

# To understand this run below
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):  # so in this line the next index till the count of n
            if arr[j] < arr[min_index]:  # if the new value is less than the current smallest value
                min_index = j  # update the index of the new smallest value
                # ✅ arr = [4, 2, 7, 1]
                # ✅ i = 0, min_index = 0 (you assume 4 is the smallest)
                # ✅ Is 2 < 4? → min_index = 1
                # ✅ Is 7 < 2? → no change
                # ✅ Is 1 < 2? → min_index = 3
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap smallest found with current i
    return arr  

arr = [4, 2, 7, 1]
print(selection_sort(arr))  # ✅ Output: [1, 2, 4, 7]


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j 
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr 

arr = [4, 2, 7, 1]
print(selection_sort(arr))

