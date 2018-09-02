def insertionSort(arr,n):
    if n<=1:
        return

    insertionSort(arr, n-1)

    last = arr[n-1]
    j=n-2

    while(j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j-=1

    arr[j+1]=last

arr = [15,1,48,97,35,68]
insertionSort(arr, len(arr))
print("sorted array is {}".format(arr))
