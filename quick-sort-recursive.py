def partition(arr,low,high):
    i=low
    pivot = arr[high]

    for j in range(low,high):
        if arr[j]<=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1

    arr[i],arr[high]=arr[high],arr[i]
    return(i)

def quickSort(arr,low,high):

    if low<high:

        pi = partition(arr,low,high)
        print(pi, low, high)
        quickSort(arr,low,pi-1)
        print(low,high)
        quickSort(arr,pi+1,high)
        print(low,high)

arr =[7,4,3,9,6]
n=len(arr)
quickSort(arr,0,n-1)
print("sorted array is {}".format(arr))
