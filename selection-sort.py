def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    print("sorted array is:")
    print(arr)

arr =[45,84,34,12,49,37,98,1]
selectionSort(arr)
