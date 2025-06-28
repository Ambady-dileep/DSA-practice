def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+n,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index]= arr[min_index],arr[i]
    return arr 

arr = [4,2,7,1]
print(selection_sort(arr))