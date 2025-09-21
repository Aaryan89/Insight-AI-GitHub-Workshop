def ascending_bubble_sort(arr):      # a bunch of logical errors
    k = len(arr)
    is_sorted = False
    while is_sorted != True:
        is_sorted = False
        for i in range(0, k):
            if arr[i] <= arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i-1] = temp
                is_sorted = False
    return arr

array = [5,6,4,1,8,10,9]                # something wrong with printing
ascending_bubble_sort(array)
print("Array before sorting: ", array)
print("Array after sorting: ", array)