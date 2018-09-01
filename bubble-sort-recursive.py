def bubbleSort(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i+1]<num:
                arr[i]=arr[i+1]
                arr[i+1]=num
                bubbleSort(arr)
        except:
            pass
    return arr

arr = [45,21,78,94,1,64,43]
bubbleSort(arr)
print("sorted array is {}".format(arr))
