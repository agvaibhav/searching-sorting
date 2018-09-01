def bubbleSort(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-j-1):
            if arr[i+1]<arr[i]:
                arr[i+1], arr[i] = arr[i], arr[i+1]

    print("sorted array is {}".format(arr))            

arr = [45,21,98,45,78,32]
bubbleSort(arr)
